def markdown_to_blocks(markdown):
    md_lst = markdown.split('\n\n')
    md_lst = [x for x in md_lst if x not in ['\n', '']]
    return md_lst