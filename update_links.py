import os

def update_links_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace all occurrences of `_en.md` with `.en.md`
    updated_content = content.replace('_en.md', '.en.md')

    # Check if any replacements were made
    if content != updated_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f"Updated links in: {file_path}")
    else:
        print(f"No links to update in: {file_path}")

def process_directory(base_directory):
    for root, _, files in os.walk(base_directory):
        for filename in files:
            if filename.endswith('.en.md'):
                file_path = os.path.join(root, filename)
                update_links_in_file(file_path)

def main():
    docs_directory = 'docs_site'  # Change this to your actual docs directory path
    process_directory(docs_directory)

if __name__ == "__main__":
    main()