from ttl.helpers.buffer import Buffer
from ttl.helpers.stack import Stack
from ttl.helpers.token import Token
from ttl.helpers.tree import Tree, Node, ValueNode


class TTLParser:
    SINGLE_OPENERS = [":"]
    MULTI_OPENERS = ["[", "{"]
    SINGLE_CLOSERS = ["\n"]
    MULTI_CLOSERS = ["]", "}"]

    ALL_OPENERS = SINGLE_OPENERS + MULTI_OPENERS
    ALL_CLOSERS = SINGLE_CLOSERS + MULTI_CLOSERS

    def __init__(self):
        self.reset()

    def reset(self):
        self.buffer = Buffer()
        self.tree = Tree()
        self.stack = Stack()
        self.stack.push(self.tree.root)

    def parse(self, content):
        self.reset()
        for char in content:
            token = Token(char)
            if self.is_opener(char):
                self.handle_opener(char)
            elif self.is_multi_closer(char):
                self.handle_closer(char)
            elif self.is_single_closer(char):
                while self.stack.peek().single_line and self.stack.not_empty():
                    self.handle_closer(char)
            else:
                self.buffer.append(char)
        return self.tree

    def is_opener(self, char):
        return char in self.ALL_OPENERS

    def is_multi_closer(self, char):
        return char in self.MULTI_CLOSERS
    
    def is_single_closer(self, char):
        return char in self.SINGLE_CLOSERS

    def handle_opener(self, char):
        single_line = char in self.SINGLE_OPENERS
        new_node = Node(self.buffer.read(), [], single_line)
        self.tree.add_child(self.stack.peek(), new_node)
        self.stack.push(new_node)

    def handle_closer(self, char):
        buffer = self.buffer.read()
        if buffer:
            self.stack.peek().children.append(ValueNode(buffer))
        self.stack.pop()