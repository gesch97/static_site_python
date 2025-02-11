from enum import Enum
from typing import Self
import re


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text} {self.text_type} {self.url})"

    @staticmethod
    def split_nodes_delimeter(
        old_nodes: list[Self], delimeter: str, text_type: TextType
    ) -> list[Self]:
        if not isinstance(old_nodes, list):
            raise TypeError(
                f"input 'old_nodes' should be a list, not {type(old_nodes)}"
            )
        if len(delimeter) <= 0:
            raise ValueError("Provided delimeter was an empty string.")

        if not isinstance(text_type, TextType):
            raise ValueError("Incorrect text_type")

        delimeter_escaped = re.escape(delimeter)
        output = list()
        for node in old_nodes:
            node_split_at_delimeters = re.split(delimeter_escaped, node.text)
            for i, piece in enumerate(node_split_at_delimeters):
                if i % 2 == 0:
                    new_textnode = TextNode(piece, node.text_type)
                else:
                    new_textnode = TextNode(piece, text_type)
                output.append(new_textnode)
        return output

    @staticmethod
    def extract_markdown_images(text: str) -> list[tuple[Self]]:
        re_pat = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(re_pat, text)
        return matches

    @staticmethod
    def extract_markdown_links(text: str) -> list[tuple[Self]]:
        re_pat = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        matches = re.findall(re_pat, text)
        return matches
