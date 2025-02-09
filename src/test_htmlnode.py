import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        text = node.props_to_html()
        self.assertEqual(text, ' href="https://www.google.com" target="_blank"')

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html2(self):
        node = HTMLNode()
        text = node.props_to_html()
        self.assertEqual(text, "")

    def test_from_text_node(self):
        text_node_normal = TextNode("asd", TextType.NORMAL)
        text_node_bold = TextNode("asd", TextType.BOLD)
        text_node_italic = TextNode("asd", TextType.ITALIC)
        text_node_code = TextNode("asd", TextType.CODE)
        text_node_link = TextNode("asd", TextType.LINK, "google.com")
        text_node_image = TextNode("A cat", TextType.IMAGE, url="cat.png")

        html_node_image = HTMLNode.from_text_node(text_node_image)
        html_node_link = HTMLNode.from_text_node(text_node_link)
        html_node_code = HTMLNode.from_text_node(text_node_code)
        html_node_italic = HTMLNode.from_text_node(text_node_italic)
        html_node_bold = HTMLNode.from_text_node(text_node_bold)
        html_node_normal = HTMLNode.from_text_node(text_node_normal)

        self.assertIsNone(html_node_normal.tag)
        self.assertEqual(html_node_normal.value, "asd")

        self.assertEqual(html_node_bold.tag, "b")
        self.assertEqual(html_node_bold.value, "asd")

        self.assertEqual(html_node_italic.tag, "i")
        self.assertEqual(html_node_italic.value, "asd")

        self.assertEqual(html_node_code.tag, "code")
        self.assertEqual(html_node_code.value, "asd")

        self.assertEqual(html_node_link.tag, "a")
        self.assertEqual(html_node_link.value, "asd")
        self.assertEqual(
            html_node_link.props,
            {
                "href": "google.com",
            },
        )

        self.assertEqual(html_node_image.tag, "img")
        self.assertEqual(html_node_image.value, "")
        self.assertEqual(
            html_node_image.props,
            {
                "src": "cat.png",
                "alt": "A cat",
            },
        )

        with self.assertRaises(ValueError):
            HTMLNode.from_text_node("not a text_node")
