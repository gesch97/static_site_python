class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        text = ""
        if self.props is None or len(self.props) == 0:
            return text
        for prop in self.props:
            text += f' {prop}="{self.props[prop]}"'

        return text

    def __repr__(self):
        text = f"""HTMLNode({self.tag} {self.value} {self.children} {self.props}"""
