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
