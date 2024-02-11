from ttl_parser import TTLParser
from ttl_renderer import TTLRenderer
import os

with open("index.ttl", "r") as f:
    test = f.read()

parser = TTLParser()
tree = parser.parse(test)
parser.print_tree(tree)
renderer = TTLRenderer("templates", tree)

with open("index2.html", "w") as f:
    f.write(renderer.render_document(tree))
