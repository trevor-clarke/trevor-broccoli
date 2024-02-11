# Trevor's Personal Website

Hello!

This is the home of my personal website.

I am aware that the name is very random, it was suggested by Github.

def recurse(self, tree):
component = tree[0]
sub_items = tree[1]

        if

        print("component", component)
        print("sub_items", sub_items)

        html = ""
        for item in sub_items:
            properties = {}
            print("item", item)
            item_key = item[0]
            for child in item[1]:
                if isinstance(child, str):
                    properties[item_key] = child
                else:
                    properties[item_key] = self.recurse(
                        child
                    )  # Ensure it's passed as a subtree

            html += self.render_template(component, properties)

        return html
