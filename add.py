import os
import sys

def create_index_files(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if "_index.md" not in filenames:
            index_path = os.path.join(dirpath, "_index.md")
            try:
                with open(index_path, 'w'):
                    pass
                print(f"Created: {index_path}")
            except Exception as e:
                print(f"Error creating {index_path}: {e}")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    create_index_files(target_dir)
