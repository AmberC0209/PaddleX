import re

def replace_links_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the regex pattern to match the English links you want to replace
    pattern = r'\.\/docs\/([a-zA-Z0-9_\/]*)_en\.md'
    replacement_pattern = r'https://amberc0209.github.io/PaddleX/latest/en/\1.html'

    # Replace the links using regex
    updated_content = re.sub(pattern, replacement_pattern, content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f'Updated links in {file_path}')

# Specify the path to your markdown file
markdown_file = 'README_en.md'

# Update the links in the specified markdown file
replace_links_in_file(markdown_file)
