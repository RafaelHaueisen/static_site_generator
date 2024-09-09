from leafnode import LeafNode

def text_node_to_html_node(text_node):
    text_type = {
        "text_type_text": "text",
        "text_type_bold": "bold",
        "text_type_italic": "italic",
        "text_type_code": "code",
        "text_type_link": "link",
        "text_type_image": "image"
    }

    if text_node.text_type not in text_type.values():
        raise Exception('Text Node type does not exist')
    
    if text_node.text_type == text_type["text_type_text"]:
        final_text = LeafNode(value=text_node.text)
    elif text_node.text_type == text_type["text_type_bold"]:
        final_text = LeafNode(tag='b', value=text_node.text)
    elif text_node.text_type == text_type["text_type_italic"]:
        final_text = LeafNode(tag='i', value=text_node.text)
    elif text_node.text_type == text_type["text_type_code"]:
        final_text = LeafNode(tag='code', value=text_node.text)
    elif text_node.text_type == text_type["text_type_link"]:
        final_text = LeafNode(tag='a', value=text_node.text, props={'href':text_node.url})
    elif text_node.text_type == text_type["text_type_image"]:
        final_text = LeafNode(tag='img', value='', props={'src':text_node.url, 'alt':text_node.text})
    
    return final_text
