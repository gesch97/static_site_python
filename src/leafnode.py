import htmlnode


class LeafNode(htmlnode.HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf must have a value")
        if self.tag == None:
            return self.value
        text = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return text
