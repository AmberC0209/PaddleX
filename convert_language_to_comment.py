import os

def replace_first_line_in_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if lines and ('简体中文 | [English]' in lines[0] or '[简体中文]' in lines[0]):
        lines[0] = '---\ncomments: true\n---\n'

        with open(filepath, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print(f'Updated: {filepath}')
    else:
        print(f'No change: {filepath}')

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                replace_first_line_in_markdown(filepath)

if __name__ == '__main__':
    directory_to_process = 'docs'  # Replace with your directory path
    process_directory(directory_to_process)