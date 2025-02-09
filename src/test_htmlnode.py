import unittest

from htmlnode import HTMLNode


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
