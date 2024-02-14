class Tree:
    def __init__(self):
        self.root = Node("root")

    def add_child(self, parent, child):
        parent.children.append(child)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if isinstance(node, ValueNode):
            shortened = node.value[:20].strip() + "..." if len(node.value) > 20 else node.value
            print("  " * level + shortened)
        else:
            print(f"{'  ' * level}[{node.name}]")
            for child in node.children:
                self.print_tree(child, level + 1)


class Node:
    def __init__(self, name, children=None, single_line=False):
        if children is None:
            children = []
        self.name = name
        self.children = children
        self.single_line = single_line

class ValueNode:
    def __init__(self, value):
        self.value = value

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def not_empty(self):
        return not self.is_empty()

class Buffer:
    def __init__(self):
        self.buffer = ""

    def read(self):
        temp = self.buffer.strip()
        self.buffer = ""
        return temp

    def append(self, char):
        self.buffer += char
    
    def not_empty(self):
        return bool(self.buffer)


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