import os
import re

def add_newline_after_table_tag(file_path):
    """Add a newline after each </table> tag in the Markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use a regular expression to find </table> tags and add a newline after them
    updated_content = re.sub(r'(</table>)', r'\1\n', content)

    # Save the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Updated </table> tags in {file_path}.")

def process_markdown_files_in_directory(directory_path):
    """Recursively process all markdown files in the specified directory and its subdirectories."""
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                print(f'Processing {file_path}...')
                add_newline_after_table_tag(file_path)
    print("All markdown files have been updated.")

# Replace 'your_directory_path' with the path to your directory
directory_path = 'docs'
process_markdown_files_in_directory(directory_path)