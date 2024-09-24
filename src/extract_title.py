from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    if not blocks or not blocks[0].startswith("# "):
        raise Exception("Please set an h1 title!")

    h1_header = blocks[0][2:]

    return h1_header