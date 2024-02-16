from ttl.helpers.buffer import Buffer
from ttl.helpers.stack import Stack
# from ttl.helpers.tree import Tree


class Tree:
    def __init__(self):
        self.root = Scope("root", "root")

    def add_child(self, parent, child):
        parent.children.append(child)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(f"{'  ' * level}[{node.type}] {node.name}")

        for child in node.children or ["-"]:
            self.print_tree(child, level + 1)


class Scope:

    # "[", "{", "(", ":"
    def determine_scope_type(opener):
        if opener == "root":
            return "root"
        elif opener == "[":
            return "list"
        elif opener == "{":
            return "body"
        elif opener == "(":
            return "properties"
        elif opener == ":":
            return "value"
        else:
            return "unknown"

    def __init__(self, opener, name, children=None):
        self.name = name
        self.children = children
        self.variables = {}
        self.type = Scope.determine_scope_type(opener)



class TokenType:
    ASSIGNMENT = 'ASSIGNMENT'
    STRING = 'STRING'
    OPENER = 'OPENER'
    CLOSER = 'CLOSER'
    ARROW = 'ARROW'


class TTLParser:
    def __init__(self):
        self.reset()

    def reset(self):
        self.buffer = Buffer()
        self.tree = Tree()
        self.stack = Stack()
        self.stack.push(self.tree.root)

    def parse(self, tokens):
        self.reset()
        for token_type, token_value in tokens:
            if token_type == TokenType.STRING:
                self.handle_string(token_value)
            elif token_type == TokenType.OPENER:
                self.handle_opener(token_value)
        return self.tree

    def handle_string(self, string):
        if self.buffer.not_empty():
            self.buffer.append(" ")
        self.buffer.append(string)
    
    def handle_opener(self, opener):
        self.stack.push(Scope(opener, self.buffer.pop()))
    
        
