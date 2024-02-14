class Token:
    SINGLE_OPENERS = [":"]
    MULTI_OPENERS = ["[", "{"]
    SINGLE_CLOSERS = [";", "\n"]
    MULTI_CLOSERS = ["]", "}"]

    ALL_OPENERS = SINGLE_OPENERS + MULTI_OPENERS

    def __init__(self, char):
        self.char = char

    @property
    def is_opener(self):
        return self.char in self.ALL_OPENERS

    @property
    def is_multi_closer(self):
        return self.char in self.MULTI_CLOSERS
    
    @property
    def is_single_closer(self):
        return self.char in self.SINGLE_CLOSERS
    
    @property
    def is_single_opener(self):
        return self.char in self.SINGLE_OPENERS