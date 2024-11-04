import os
import re

def update_links_in_markdown_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 查找匹配的链接
    matches = re.findall(r'(_en\.md)', content)
    
    if matches:
        print(f'Found {len(matches)} links to update in {file_path}')
    else:
        print(f'No links to update in {file_path}')
    
    # 使用正则表达式查找并替换链接
    updated_content = re.sub(r'(_en\.md)', r'.en.md', content)

    # 如果内容有变化，则写回文件
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f'Updated links in {file_path}')
    else:
        print(f'No changes made to {file_path}')

def process_directory(directory):
    # 遍历目录和子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                update_links_in_markdown_file(file_path)

if __name__ == '__main__':
    # 指定你的Markdown文件所在的根目录
    root_directory = 'docs'
    process_directory(root_directory)