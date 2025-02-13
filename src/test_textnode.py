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

    def test_extract_markdown_images(self):
        list_of_images = TextNode.extract_markdown_images(
            (
                "This is text with a "
                "![rick roll](https://i.imgur.com/aKaOqIh.gif)"
                "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
            )
        )
        self.assertIsInstance(list_of_images, list)
        self.assertEqual(
            list_of_images,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

        list_of_images_empty = TextNode.extract_markdown_images("asd")
        self.assertEqual(list_of_images_empty, list())

    def test_extract_markdown_links(self):
        text = (
            "This is text with a link [to boot dev](https://www.boot.dev)"
            "and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        list_of_links = TextNode.extract_markdown_links(text)
        self.assertEqual(
            list_of_links,
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )
        list_of_links_empty = TextNode.extract_markdown_links("asd")
        self.assertEqual(list_of_links_empty, list())

    def test_split_nodes_image(self):
        node = TextNode("text ![img_text](img_link)", TextType.NORMAL)
        node2 = TextNode("there is no image here", TextType.NORMAL)

        new_nodes = TextNode.split_nodes_image([node])
        new_nodes2 = TextNode.split_nodes_image([node2])

        result = [
            TextNode("text ", TextType.NORMAL),
            TextNode("img_text", TextType.IMAGE, url="img_link"),
        ]
        result2 = [TextNode("there is no image here", TextType.NORMAL)]

        self.assertEqual(new_nodes, result)
        self.assertEqual(new_nodes2, result2)

    def test_split_nodes_links(self):
        node = TextNode(
            "text [alt_text1](link1) txt_after",
            TextType.NORMAL,
        )
        node2 = TextNode("[alt1](link1)[alt2](link2)[text_in_bracket]", TextType.NORMAL)
        node3 = TextNode("text [alt1](link1)", TextType.NORMAL)
        node4 = TextNode("text no link", TextType.ITALIC)
        node5 = TextNode("image no link", TextType.IMAGE, url="image_URL.com")

        new_nodes = TextNode.split_nodes_links([node])
        new_nodes2 = TextNode.split_nodes_links([node, node2])
        new_nodes3 = TextNode.split_nodes_links([node3])
        new_nodes4 = TextNode.split_nodes_links([node4])
        new_nodes5 = TextNode.split_nodes_links([node5])

        result = [
            TextNode("text ", TextType.NORMAL),
            TextNode("alt_text1", TextType.LINK, "link1"),
            TextNode(" txt_after", TextType.NORMAL),
        ]
        result2 = [
            TextNode("alt1", TextType.LINK, url="link1"),
            TextNode("alt2", TextType.LINK, url="link2"),
            TextNode("[text_in_bracket]", TextType.NORMAL),
        ]
        result3 = [
            TextNode("text ", TextType.NORMAL),
            TextNode("alt1", TextType.LINK, url="link1"),
        ]

        self.assertEqual(new_nodes, result)
        self.assertEqual(new_nodes2, result + result2)
        self.assertEqual(new_nodes3, result3)
        self.assertEqual(new_nodes4, [node4])
        self.assertEqual(new_nodes5, [node5])
