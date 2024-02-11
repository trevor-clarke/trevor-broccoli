import re
import os

TTL_FILE_EXTENSION = ".ttl"


# test = """
# section [
#     title {
#         Outer section title
#     }
#     body{
#         section [
#             title {
#                 Inner section title
#             }
#             body{
#                 Inner Body
#             }
#         ]
#     }
# ]
# """


test = """
section [
    title {
        Outer section title
    }
    body{
        section [
            title {
                Inner section title
            }
            body{
               section [
                    title {
                        Inner section title
                    }
                    body{
                        Inner Body
                    }
                ]
            }
        ]
    }
]
section [
                    title {
                        Section on its own
                    }
                    body{
                        Inner Body of section on its own
                    }
                ]
    red [
        body {
            This is a red box
        }
    ]
"""


def parser(content):
    buffer = ""
    root = ("root", [])
    stack = [root]

    for char in content:
        buffer = buffer.strip()
        if char == "[":
            # print("Entering: ", buffer)
            new = (buffer, [])
            buffer = ""
            stack[-1][1].append(new)
            stack.append(new)
        elif char == "]":
            # print("Exiting:  ", buffer)
            stack.pop()
        elif char == "{":
            # print("Entering: ", buffer)
            new = (buffer, [])
            buffer = ""
            stack[-1][1].append(new)
            stack.append(new)
        elif char == "}":
            # print("Exiting:  ", buffer)
            stack[-1][1].append(buffer)
            buffer = ""
            stack.pop()
        else:
            buffer += char

    return root


def print_tree(tree, level=0):
    if isinstance(tree, str):
        print("  " * level, tree)
    else:
        print("  " * level, tree[0])
        for child in tree[1]:
            print_tree(child, level + 1)


class Renderer:
    def __init__(self, template_directory, tree):
        self.template_directory = template_directory
        self.tree = tree
        self.templates = self.load_template()

    def load_template(self):
        templates = {}
        for file in os.listdir(self.template_directory):
            if file.endswith(TTL_FILE_EXTENSION):
                name = file.split(".")[0]
                with open(self.template_directory + "/" + file, "r") as f:
                    templates[name] = f.read()
        return templates

    def render_template(self, key, properties):
        template_copy = self.templates[key]
        for key, value in properties.items():
            pattern = re.compile(r"\{\{\s*" + re.escape(key) + r"\s*\}\}")
            template_copy = pattern.sub(value, template_copy)
        return template_copy

    def recurse(self, tree):

        component = tree[0]
        children = tree[1]

        properties = {}
        for child in children:
            # child at this point should be a tuple
            child_key = child[0]
            child_value = child[1][0]

            if isinstance(child_value, str):
                properties[child_key] = child_value
            else:
                properties[child_key] = self.recurse(child_value)

        return self.render_template(component, properties)

    def generate_html(self, tree):
        html = ""
        for child in tree[1]:
            html += self.recurse(child)
        return html


tree = parser(test)
# print(tree)
# html = generate_html(tree)
# print(html)

renderer = Renderer("templates", tree)
print("Okay:", renderer.generate_html(tree))

# print_tree(parser(test))
