import re
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_to_html_converter import text_node_to_html_node

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    children = []

    for block in md_blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    
    return ParentNode(tag="div", children=children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    if block_type == "heading":
        return heading_to_html_node(block)
    if block_type == "code":
        return code_to_html_node(block)
    if block_type == "ordered_list":
        return olist_to_html_node(block)
    if block_type == "unordered_list":
        return ulist_to_html_node(block)
    if block_type == "quote":
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode(tag="p", children=children)

def heading_to_html_node(block):
    rash_match = re.match(r"^#{1,6} ", block)
    rash_match_num = len(rash_match.group(0)) - 1

    new_block = re.sub(r"^#{1,6} ", "", block)
    lines = new_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode(tag=f"h{rash_match_num}", children=children)

def code_to_html_node(block):
    new_block = re.sub(r"^``` ?|```$", "", block)
    lines = new_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)

    code = [ParentNode(tag="code", children=children)]
    return ParentNode(tag="pre", children=code)

def olist_to_html_node(block):
    lines = block.split("\n")
    children = []

    for line in lines:
        new_line = re.sub(r"^\d+\. ", "", line)
        leaf = text_to_children(new_line)
        children.append(ParentNode(tag="li", children=leaf))

    return ParentNode(tag="ol", children=children)

def ulist_to_html_node(block):
    lines = block.split("\n")
    children = []

    for line in lines:
        new_line = re.sub(r"^(\* |\- )", "", line)
        leaf = text_to_children(new_line)
        children.append(ParentNode(tag="li", children=leaf))

    return ParentNode(tag="ul", children=children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []

    for line in lines:
        new_line = re.sub(r"^\> ?", "", line)
        new_lines.append(new_line)

    paragraph = " ".join(new_lines)
    children = text_to_children(paragraph)
    
    return ParentNode(tag="blockquote", children=children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for node in text_nodes:
        children.append(text_node_to_html_node(node))

    return children