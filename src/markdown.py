import enum
import re


class BlockType(enum.Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    NORMAL = "normal"


def markdown_to_blocks(markdown: str) -> list[str]:
    if not isinstance(markdown, str):
        raise ValueError("Input should be string")
    output = list()
    blocks = markdown.split("\n\n")
    for block in blocks:
        without_trailing_or_leading_white_space = block.lstrip().rstrip()
        if len(without_trailing_or_leading_white_space) == 0:
            continue
        output.append(without_trailing_or_leading_white_space)

    return output


def block_to_block_type(block: str):
    if not isinstance(block, str):
        raise TypeError("input should be string")

    re_pat_heading = r"#{1,6}[ ].*"
    if re.fullmatch(re_pat_heading, block) is not None:
        return BlockType.HEADING

    re_pat_code = r"^`{3}.*`{3}"
    if re.fullmatch(re_pat_code, block) is not None:
        return BlockType.CODE

    re_pat_quote = r"^>.*"
    if re.match(re_pat_quote, block, flags=re.MULTILINE) is not None:
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return BlockType.NORMAL
        return BlockType.QUOTE

    re_pat_u_ordered_list = r"^\*.*"
    if re.match(re_pat_u_ordered_list, block, flags=re.MULTILINE) is not None:
        lines = block.split("\n")
        for line in lines:
            if not line.startswith("* "):
                return BlockType.NORMAL
        return BlockType.UNORDERED_LIST

    re_pat_ordered_list = r"^\d\.\s.*\n"
    if re.match(re_pat_ordered_list, block, flags=re.MULTILINE) is not None:
        lines = block.split("\n")
        for i, line in enumerate(lines):
            if not line.startswith(str(i + 1)):
                return BlockType.NORMAL
        return BlockType.ORDERED_LIST

    return BlockType.NORMAL
