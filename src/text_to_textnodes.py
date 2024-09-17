from textnode import TextNode
from split_nodes_from_images_links import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_to_textnodes(text):
    node = TextNode(text, "text")
    bold = split_nodes_delimiter([node], "**", text_type_bold)
    italic = split_nodes_delimiter(bold, "*", text_type_italic)
    code = split_nodes_delimiter(italic, "`", text_type_code)
    image_nodes = split_nodes_image(code)
    final_format_nodes = split_nodes_link(image_nodes)
    return final_format_nodes