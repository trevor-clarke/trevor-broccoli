class TTLParser:
    def __init__(self):
        self.buffer = ""
        self.root = ("root", [])
        self.stack = []

    def reset(self):
        self.buffer = ""
        self.root = ("root", [])
        self.stack = [self.root]
        self.single_line = False

    def parse(self, content):
        self.reset()
        switch = {
            ":": self.handle_colon,
            "[": self.handle_bracket,
            "{": self.handle_brace,
            "\n": self.handle_newline,
            ";": self.handle_semicolon,
            "]": self.handle_close_bracket,
            "}": self.handle_close_brace
        }
        for char in content:
            func = switch.get(char, self.handle_default)
            func(char)
        return self.root

    def handle_colon(self, char):
        self.single_line = True
        self.handle_open(char)

    def handle_bracket(self, char):
        self.handle_open(char)

    def handle_brace(self, char):
        self.handle_open(char)

    def handle_newline(self, char):
        if self.single_line:
            self.single_line = False
            self.handle_close(char)

    def handle_semicolon(self, char):
        if self.single_line:
            self.single_line = False
            self.handle_close(char)

    def handle_close_bracket(self, char):
        self.handle_close(char)

    def handle_close_brace(self, char):
        self.handle_close(char)

    def handle_open(self, char):
        new_node = (self.buffer.strip(), [])
        self.buffer = ""
        self.stack[-1][1].append(new_node)
        self.stack.append(new_node)

    def handle_close(self, char):
        if self.buffer.strip():
            self.stack[-1][1].append(self.buffer.strip())
            self.buffer = ""
        self.stack.pop()

    def handle_default(self, char):
        self.buffer += char

    def print_tree(self, tree=None, level=0):
        if tree is None:
            tree = self.root
        if isinstance(tree, str):
            shortened = tree[:20].strip() + "..." if len(tree) > 20 else tree
            print("  " * level + shortened)
        else:
            print(f"{'  ' * level}[{tree[0]}]")
            for child in tree[1]:
                self.print_tree(child, level + 1)
