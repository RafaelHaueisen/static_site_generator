import os
import shutil

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
    source_dir = 'static'
    destination_dir = 'public'
    copy_directory(source_dir, destination_dir)

if __name__ == "__main__":
    main()