from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node should have a tag.")
        if self.children is None:
            raise ValueError("Parent Node should have a children.")

        children_string = "".join(
            list(map(lambda child: child.to_html(), self.children))
        )
        text = f"<{self.tag}>{children_string}</{self.tag}>"

        return text
