import os
import re

from ttl.helpers.node import Node, ValueNode

TTL_FILE_EXTENSION = ".ttl"

#pass in arrray of properties to initaliszer 
# 


class Template:
    def __init__(self, name, html, css, properties):
        self.name = name
        self.html = html
        self.css = css
        self.properties = properties

    VARIABLE_PATTERN = re.compile(r"\{\{\s*(\w+)\s*\}\}")

    def render(self, props):
        html = self.html+""
        invalid_properties = set(props.keys()) - set(self.properties)
        if invalid_properties:
            raise ValueError(f"Invalid properties: {invalid_properties.keys()}")

        for property in self.properties:
            value = props.get(property) or ""
            pattern = re.compile(r"\{\{\s*" + re.escape(property) + r"\s*\}\}")
            html = pattern.sub(value, html)
        return html

   
    @staticmethod
    def from_file(file_path):
        with open(file_path, "r") as f:
            template_content = f.read()

        css_pattern = re.compile(r"<style>(.*?)</style>", re.DOTALL)
        css = "\n".join(css_pattern.findall(template_content))
        html = re.sub(css_pattern, "", template_content).strip()

        name = os.path.basename(file_path).split(".")[0]

        properties = re.findall(Template.VARIABLE_PATTERN, html)

        return Template(name, html, css, properties)


class Templates:
    def __init__(self, template_directory):
        self.template_directory = template_directory
        self.templates = self.load_templates()
        self.used_templates = set()

    def load_templates(self):
        templates = {}
        for file in os.listdir(self.template_directory):
            if file.endswith(TTL_FILE_EXTENSION):
                template = Template.from_file(os.path.join(self.template_directory, file))
                templates[template.name] = template
        return templates

    def get(self, name):
        template = self.templates.get(name)
        if template:
            self.used_templates.add(name)
        if template is None:
            if len(name) > 1:
                return self.get(name[0:1])
            raise ValueError(f"Template {name} not found")
        return template

    def generate_css(self):
        css = ""
        for template_name in self.used_templates:
            css += self.templates.get(template_name).css
        return f"{css}\n"