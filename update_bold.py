import os
import re

def convert_bold_to_html(directory):
    # 定义正则表达式以匹配 Markdown 中的加粗文本
    bold_pattern = re.compile(r'\*\*(.*?)\*\*')

    # 遍历目录及其子目录
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找并替换 Markdown 加粗文本为 HTML 格式
                new_content = bold_pattern.sub(r'<b>\1</b>', content)
                
                # 如果内容发生变化则写回文件
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated bold text in: {file_path}")

# 使用函数，替换 'your_directory_path' 为你的目标目录路径
convert_bold_to_html('docs')