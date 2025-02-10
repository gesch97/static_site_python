import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("asd", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_def_value(self):
        node = TextNode("asd", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_split_nodes_delimeter(self):
        with self.assertRaises(TypeError):
            TextNode.split_nodes_delimeter("not a list", "a", TextType.NORMAL)

        with self.assertRaises(ValueError):
            TextNode.split_nodes_delimeter(
                [
                    TextNode("a", TextType.NORMAL),
                ],
                "",
                TextType.NORMAL,
            )

        with self.assertRaises(ValueError):
            TextNode.split_nodes_delimeter(
                [
                    TextNode("a", TextType.NORMAL),
                ],
                "*",
                "not a texttype",
            )

        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        node_split = TextNode.split_nodes_delimeter(
            [
                node,
            ],
            "`",
            TextType.CODE,
        )
        should_return = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]

        self.assertEqual(node_split, should_return)

        node2 = TextNode("aa 'bb' cc' dd", TextType.NORMAL)
        node_split2 = TextNode.split_nodes_delimeter(
            [
                node2,
            ],
            "'",
            TextType.CODE,
        )
        should_return2 = [
            TextNode("aa ", TextType.NORMAL),
            TextNode("bb", TextType.CODE),
            TextNode(" cc", TextType.NORMAL),
            TextNode(" dd", TextType.CODE),
        ]
        self.assertEqual(node_split2, should_return2)


if __name__ == "__main__":
    unittest.main()
