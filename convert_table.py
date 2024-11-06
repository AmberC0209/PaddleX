import os
import re
from markdown import markdown

def convert_markdown_table_to_html(markdown_content):
    """Convert markdown tables to HTML tables."""
    # Use markdown with tables extension to convert markdown table to HTML
    return markdown(markdown_content, extensions=['tables'])

def find_and_convert_tables(content):
    """Find markdown tables in the content and convert them to HTML."""
    # Regular expression to match Markdown tables
    table_regex = re.compile(r'(^\|.*?\|\s*$\n?)+', re.MULTILINE)

    def convert_table(match):
        table_markdown = match.group(0)
        table_html = convert_markdown_table_to_html(table_markdown)
        return table_html + '\n'  # Add a newline after the converted HTML table

    # Substitute markdown tables with HTML tables
    new_content = table_regex.sub(convert_table, content)

    return new_content

def process_markdown_file(file_path):
    """Process a single markdown file, converting tables to HTML."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find and convert tables to HTML
    converted_content = find_and_convert_tables(content)

    # Save the converted content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(converted_content)
    
    print(f"Converted tables in {file_path} to HTML successfully.")

def process_markdown_files_in_directory(directory_path):
    """Recursively process all markdown files in the specified directory and its subdirectories."""
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                print(f'Processing {file_path}...')
                process_markdown_file(file_path)
    print("All markdown files have been processed.")

# Replace 'your_directory_path' with the path to your directory
directory_path = 'docs'
process_markdown_files_in_directory(directory_path)