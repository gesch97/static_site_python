import unittest
from markdown import markdown_to_blocks


class test_markdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is a heading

        This is a paragraph of text. It has some ** bold ** and *italic * words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""

        md2 = "\n\n\n\n   "

        result = markdown_to_blocks(md)
        result2 = markdown_to_blocks(md2)

        expected_result = [
            "This is a heading",
            "This is a paragraph of text. It has some ** bold ** and *italic * words inside of it.",
            """* This is the first list item in a list block
        * This is a list item
        * This is another list item""",
        ]

        expected_result2 = []

        self.assertEqual(result, expected_result)
        self.assertEqual(result2, expected_result2)
