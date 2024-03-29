from .ttl_parser import TTLParser
from .ttl_renderer import TTLRenderer


class TTL:
    def __init__(self, template_dir):
        self.parser = TTLParser()
        self.renderer = TTLRenderer(template_dir)

    def process(self, input_file, output_file, tree=False):
        with open(input_file, "r") as i:
            tree = self.parser.parse(i.read())
            if tree:
                tree.print_tree()
            html = self.renderer.render_document(tree.root)

        with open(output_file, "w") as o:
            o.write(html)
