import os
import re
import markdown

def convert_specific_markdown_to_html(content):
    """Convert markdown tables, bold text, lists, and code blocks to HTML within <details>."""
    # 去除所有行的前导空格或制表符，但保留代码块的缩进
    lines = content.split('\n')
    cleaned_lines = []
    in_code_block = False

    for line in lines:
        if line.startswith("```"):
            in_code_block = not in_code_block
        
        # 如果不在代码块中，去除行首的空格或制表符
        if not in_code_block:
            cleaned_lines.append(line.lstrip())
        else:
            cleaned_lines.append(line)

    content = '\n'.join(cleaned_lines)

    # Convert markdown tables, allowing for leading spaces or tabs
    table_pattern = re.compile(r'(?:^[ \t]*\|.*\|.*\|\s*$\n?)+', re.MULTILINE)
    content = table_pattern.sub(lambda match: markdown.markdown(match.group(0), extensions=['tables']), content)

    # Convert markdown bold text
    bold_pattern = re.compile(r'(\*\*|__)(.*?)\1')
    content = bold_pattern.sub(r'<strong>\2</strong>', content)

    # Convert markdown lists and code blocks
    # Use markdown to convert lists and code blocks
    content = markdown.markdown(content, extensions=['fenced_code', 'tables'])

    return content

def process_file(file_path):
    """Process a single markdown file to convert specific content in <details>."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to find <details> tags
    pattern = r'(<details>)(.*?)(</details>)'

    def replacer(match):
        """Replace markdown tables, bold text, lists, and code blocks within <details> with HTML content."""
        details_start, markdown_content, details_end = match.groups()
        # Convert the specific markdown content to HTML
        html_content = convert_specific_markdown_to_html(markdown_content.strip())
        return f"{details_start}{html_content}{details_end}"

    # Replace all occurrences of <details> specific markdown content
    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_directory(directory):
    """Recursively process all markdown files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                process_file(file_path)

if __name__ == "__main__":
    directory_path = "docs"
    process_directory(directory_path)
