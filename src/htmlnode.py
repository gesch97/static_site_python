from textnode import TextNode, TextType


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

    @classmethod
    def from_text_node(cls, text_node: TextNode):
        if not isinstance(text_node, TextNode):
            raise ValueError(f"text_node should be TextNode, not: {type(text_node)}")

        match text_node.text_type:
            case TextType.NORMAL:
                return cls(value=text_node.text)
            case TextType.BOLD:
                return cls(tag="b", value=text_node.text)
            case TextType.ITALIC:
                return cls(tag="i", value=text_node.text)
            case TextType.CODE:
                return cls(tag="code", value=text_node.text)
            case TextType.LINK:
                return cls(tag="a", value=text_node.text, props={"href": text_node.url})
            case TextType.IMAGE:
                return cls(
                    tag="img",
                    value="",
                    props={
                        "src": text_node.url,
                        "alt": text_node.text,
                    },
                )
            case _:
                raise ValueError("Unknow TextType")
