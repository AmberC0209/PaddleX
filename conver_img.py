import os
import re

def convert_markdown_to_html_images(directory):
    # 正则表达式匹配Markdown图片链接
    markdown_img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    # 遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # 确保是Markdown文件
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                
                # 替换Markdown图片链接为HTML格式
                new_content = markdown_img_pattern.sub(r'<img src="\1">', content)
                
                with open(file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(new_content)
                print(f'Converted {file_path}')

# 使用示例
# 请将'your_directory_path'替换为你的目录路径
convert_markdown_to_html_images('your_directory_path')