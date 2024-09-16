from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_type_text = "text"
    final_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            new_nodes = node.text.split(delimiter)
            if len(new_nodes) % 2 == 0:
                raise Exception('Error! Missing matching delimiter.')
            else:
                for i in range(len(new_nodes)):
                    if i % 2 == 0:
                        new_nodes[i] = TextNode(new_nodes[i], text_type_text)
                    else:
                        new_nodes[i] = TextNode(new_nodes[i], text_type)
            new_nodes = [x for x in new_nodes if x.text != '']
            final_nodes.extend(new_nodes)
        else:
            final_nodes.append(node)
    return final_nodes
