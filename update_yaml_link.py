import re

def replace_yaml_links_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the regex pattern to match the YAML links you want to replace
    pattern = r'\.\.\/\.\.\/(paddlex\/configs\/[a-zA-Z0-9_\/]+\.yaml)'
    replacement_pattern = r'https://github.com/PaddlePaddle/PaddleX/blob/develop/\1'

    # Replace the links using regex
    updated_content = re.sub(pattern, replacement_pattern, content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f'Updated YAML links in {file_path}')

# Specify the path to your markdown file
markdown_file = './docs/support_list/models_list.en.md'

# Update the YAML links in the specified markdown file
replace_yaml_links_in_file(markdown_file)