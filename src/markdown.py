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
