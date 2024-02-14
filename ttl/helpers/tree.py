from .node import Node, ValueNode

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
