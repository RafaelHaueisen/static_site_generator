import os
import shutil
from genpage import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def copy_directory(src, dst):
    # Delete the destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    # Create the destination directory
    os.mkdir(dst)

    # Recursively copy contents from src to dst
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            # Copy file
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} -> {dst_path}")
        elif os.path.isdir(src_path):
            # Copy directory recursively
            os.mkdir(dst_path)
            print(f"Created directory: {dst_path}")
            copy_directory(src_path, dst_path)  # Recurse into subdirectory

def main():
    copy_directory(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()