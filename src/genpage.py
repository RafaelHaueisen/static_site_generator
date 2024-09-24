import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        from_contents = file.read()

    with open(template_path, "r") as file:
        template_contents = file.read()

    md_to_html = markdown_to_html_node(from_contents)
    md_to_html = md_to_html.to_html()

    title = extract_title(from_contents)

    full_html_page = template_contents.replace("{{ Title }}", title)
    full_html_page = full_html_page.replace("{{ Content }}", md_to_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(full_html_page)