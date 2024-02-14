import re
from ttl.helpers.node import Node, ValueNode
from .ttl_templates import Templates


class TTLRenderer:
    def __init__(self, template_directory):
        self.templates = Templates(template_directory)

    def render_template(self, key, properties):
        template = self.templates.get(key)
        print(template, key, properties)

        props_hash = {}
        for node in properties:
            children = node.children
            property = node.name
            if len(children) == 1 and isinstance(children[0], ValueNode):
                props_hash[property] =  children[0].value
            else:
                html = "".join(
                    [
                        self.render_tree(value) if isinstance(value, Node) else value.value
                        for value in children
                    ]
                )
                props_hash[property] = html

        return template.render(props_hash)

    def render_tree(self, tree):
        return self.render_template(tree.name, tree.children)

    def render_document(self, tree):
        body = "".join([self.render_tree(child) for child in tree.children])
        indented_body = "\n".join([f"\t{line}" for line in body.splitlines()])
        
        css = self.templates.generate_css()
        indented_css = "\n".join([f"\t{line}" for line in css.splitlines()])

        root_template = self.templates.get("root")
        return root_template.render({"body": indented_body, "css": indented_css})