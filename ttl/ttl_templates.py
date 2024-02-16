import os
import re

from ttl.helpers.node import Node, ValueNode

TTL_FILE_EXTENSION = ".ttl"


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

    HTML_TAGS =html_tags = ["!DOCTYPE", "a", "abbr", "acronym", "address", "applet", "area", "article", "aside", "audio", "b", "base", "basefont", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "font", "footer", "form", "frame", "frameset", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noframes", "noscript", "object", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "script", "section", "select", "small", "source", "span", "strike", "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt", "u", "ul", "var", "video", "wbr"]
    
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

        # now load all html tags as templates (eg: body)
        for tag in self.HTML_TAGS:
            template = Template(tag, f"<{tag}>{{{{body}}}}</{tag}>", "", ["body"])
            templates[tag] = template

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
    