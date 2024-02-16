TOKENS = {
    "OPENERS": ["[", "{", "(", ":"],
    "CLOSERS": ["]", "}", ")", ";"],
    "EQUALS": "=",
    "COMMA": ",",
    "ARROW": "->",
    "WHITESPACE": " ",
    "QUOTE": "\""
}

ALL_TOKENS = [token for sublist in TOKENS.values() for token in sublist]

class Tokenizer:
    def __init__(self, content):
        self.content = content
        self.position = 0

    def next_token(self):
        while self.position < len(self.content):
            char = self.content[self.position]
            self.position += 1

            if char in TOKENS["WHITESPACE"]:
                continue
            elif char in TOKENS["OPENERS"]:
                return ("OPENER", char)
            elif char in TOKENS["CLOSERS"]:
                return ("CLOSER", char)
            elif char == TOKENS["EQUALS"]:
                return ("EQUALS", char)
            elif char == TOKENS["COMMA"]:
                return ("COMMA", char)
            elif char == TOKENS["QUOTE"]:
                return ("QUOTE", char)
            elif self.content[self.position-1:self.position+1] == TOKENS["ARROW"]:
                self.position += 1  # Skip the next character
                return ("ARROW", TOKENS["ARROW"])
            else:
                # Build up a string until we hit a character that we know
                start = self.position - 1
                while (self.position < len(self.content) and 
                          self.content[self.position] not in ALL_TOKENS and
                            self.content[self.position-1:self.position+1] != TOKENS["ARROW"]):
                    self.position += 1
                return ("STRING", self.content[start:self.position])
        return ("EOF", None)

    def get_tokens(self):
        tokens = []
        while (token := self.next_token())[0] != "EOF":
            tokens.append(token)
        return tokens

