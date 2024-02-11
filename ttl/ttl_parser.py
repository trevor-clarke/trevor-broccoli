class TTLParser:
    def __init__(self):
        self.buffer = ""
        self.root = ("root", [])
        self.stack = []

    def reset(self):
        self.buffer = ""
        self.root = ("root", [])
        self.stack = [self.root]

    def parse(self, content):
        self.reset()
        for char in content:
            if char in ["[", "{"]:
                new_node = (self.buffer.strip(), [])
                self.buffer = ""
                self.stack[-1][1].append(new_node)
                self.stack.append(new_node)
            elif char in ["]", "}"]:
                if self.buffer.strip():
                    self.stack[-1][1].append(self.buffer.strip())
                    self.buffer = ""
                self.stack.pop()
            else:
                self.buffer += char
        return self.root

    def print_tree(self, tree=None, level=0):
        if tree is None:
            tree = self.root
        if isinstance(tree, str):
            print("  " * level + tree)
        else:
            print("  " * level + tree[0])
            for child in tree[1]:
                self.print_tree(child, level + 1)
