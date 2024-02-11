from ttl_parser import TTLParser
from ttl_renderer import TTLRenderer
import os

parser = TTLParser()
renderer = TTLRenderer("templates")

with open("index.ttl", "r") as i:
    with open("index2.html", "w") as o:
        tree = parser.parse(i.read())
        parser.print_tree()
        html = renderer.render_document(tree)
        o.write(html)
