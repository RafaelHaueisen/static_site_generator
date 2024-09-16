from textnode import TextNode
from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links

text_type_text = "text"
text_type_link = "link"
text_type_image = "image"

def split_nodes(extract_func, text_type):
    def inner_split_nodes(old_nodes):
        final_nodes = []
        if not old_nodes:
            return final_nodes
        for node in old_nodes:
            img_or_lnk_lst = extract_func(node.text)
            if img_or_lnk_lst == []:
                    final_nodes.append(node)
                    continue
            
            img_or_lnk_name, img_or_lnk_per_se = img_or_lnk_lst[0]
            if text_type == "link":
                split_pattern = f"[{img_or_lnk_name}]({img_or_lnk_per_se})"
            else:
                split_pattern = f"![{img_or_lnk_name}]({img_or_lnk_per_se})"
            new_nodes = node.text.split(split_pattern, 1)

            final_nodes.append(TextNode(new_nodes[0], text_type_text))
            final_nodes.append(TextNode(img_or_lnk_name, text_type, img_or_lnk_per_se))
            remaining_text = new_nodes[1]
            
            if remaining_text:
                final_nodes.extend(inner_split_nodes([TextNode(remaining_text, text_type_text)]))
            final_nodes = [x for x in final_nodes if x.text != '']

        return final_nodes
    return inner_split_nodes

split_nodes_image = split_nodes(extract_markdown_images, text_type_image)
split_nodes_link = split_nodes(extract_markdown_links, text_type_link)



