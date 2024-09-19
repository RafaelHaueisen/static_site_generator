def markdown_to_blocks(markdown):
    md_lst = markdown.split('\n\n')
    md_lst = [x for x in md_lst if x not in ['\n', '']]
    filtered_lst = []
    for md in md_lst:
        md = md.strip()
        filtered_lst.append(md)
    return filtered_lst