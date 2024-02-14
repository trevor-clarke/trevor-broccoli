import re
from ttl.helpers.node import Node, ValueNode
from .ttl_templates import Templates


class TTLRenderer:
    def __init__(self, template_directory):
        self.templates = Templates(template_directory)

    def render_document(self, tree):
        body = "".join([self.render_template(child) for child in tree.children])
        indented_body = self._indent_lines(body)

        css = self.templates.generate_css()
        indented_css = self._indent_lines(css)

        root_template = self.templates.get("root")
        return root_template.render({"body": indented_body, "css": indented_css})

    def render_template(self, tree):
        key = tree.name
        properties = tree.children
        template = self.templates.get(key)
        values = self._prop_array_to_hash(properties)
        return template.render(values)

    def _prop_array_to_hash(self, properties):
        values = {}
        for node in properties:
            property = node.name
            children = node.children
            if len(children) == 1 and isinstance(children[0], ValueNode):
                values[property] = children[0].value
            else:
                values[property] = self._get_html_from_children(children)
        return values
        
    def _get_html_from_children(self, children):
        return "".join(
            [self.render_template(value) if isinstance(value, Node) else value.value for value in children]
        )

    def _indent_lines(self, text, indent="\t"):
        return "\n".join([f"{indent}{line}" for line in text.splitlines()])