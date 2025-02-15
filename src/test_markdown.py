import unittest
from markdown import markdown_to_blocks, block_to_block_type, BlockType


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

    def test_markdown_to_blocks(self):
        test_cases = [
            ("#This not a heading", BlockType.NORMAL),
            ("# This a heading", BlockType.HEADING),
            ("## This a heading", BlockType.HEADING),
            ("#### This a heading", BlockType.HEADING),
            ("##### This a heading", BlockType.HEADING),
            ("###### This a heading", BlockType.HEADING),
            ("``` This a code block```", BlockType.CODE),
            ("`` This a code block```", BlockType.NORMAL),
            ("``` This a code block``", BlockType.NORMAL),
            ("> This a single line of quote", BlockType.QUOTE),
            ("> This a single line of quote\n>This a second one", BlockType.QUOTE),
            ("> This a single line of quote\nThis a second one", BlockType.NORMAL),
            ("* This an unordered list element", BlockType.UNORDERED_LIST),
            ("* This an unordered list element\n* asd", BlockType.UNORDERED_LIST),
            ("* This an unordered list element\n asd", BlockType.NORMAL),
            ("1. first\n2. second\n3. third", BlockType.ORDERED_LIST),
            ("1. first\n4. second\n3. third", BlockType.NORMAL),
            ("This\n is a normal\n block", BlockType.NORMAL),
        ]

        for test_case in test_cases:
            res = block_to_block_type(test_case[0])
            self.assertEqual(res, test_case[1])
