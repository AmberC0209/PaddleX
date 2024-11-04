import os

def rename_files_recursively(base_directory):
    for root, _, files in os.walk(base_directory):
        for filename in files:
            # Check if the file ends with '_en.md'
            if filename.endswith('_en.md'):
                new_filename = filename.replace('_en.md', '.en.md')
                old_file = os.path.join(root, filename)
                new_file = os.path.join(root, new_filename)
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} -> {new_file}")

def main():
    docs_directory = 'docs'  # Change this to your actual docs directory path
    rename_files_recursively(docs_directory)

if __name__ == "__main__":
    main()
