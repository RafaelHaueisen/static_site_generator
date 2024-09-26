import os
from pathlib import Path
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

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