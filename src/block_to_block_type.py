def block_to_block_type(md_block):
    lines = md_block.split("/n")
    
    if (md_block.startswith("# ") 
        or md_block.startswith("## ")
        or md_block.startswith("### ")
        or md_block.startswith("#### ")
        or md_block.startswith("##### ")
        or md_block.startswith("###### ")):
        return "heading"
    elif md_block.startswith("```") and md_block.startswith("```", -3):
        return "code"
    elif md_block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return "paragraph"
        return "quote"
    elif md_block.startswith("* ") or md_block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not md_block.startswith("- "):
                return "paragraph"
        return "unordered_list"
    elif md_block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    else:
        return "paragraph"