import os
import requests
from bs4 import BeautifulSoup
import markdown
from urllib.parse import urlparse
import random
import string
import hashlib
from datetime import datetime

def generate_md5_filename(file_content, file_ext):
    """Generate a file name based on the MD5 hash of the file content"""
    md5_hash = hashlib.md5(file_content).hexdigest()
    return md5_hash + file_ext

def download_image(image_url, save_folder):
    """Download an image and save it to the specified folder"""
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Confirm successful request
        file_content = response.content
        file_ext = os.path.splitext(urlparse(image_url).path)[1]
        file_name = generate_md5_filename(file_content, file_ext)
        save_path = os.path.join(save_folder, file_name)
        with open(save_path, 'wb') as f:
            f.write(file_content)
        return file_name  # Return the new file name
    except Exception as e:
        print(f"Download failed for {image_url}, Error: {e}")
        return None

def update_md_file(md_path, base_image_folder):
    """更新Markdown文件中的图片链接"""
    with open(md_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # 使用BeautifulSoup来解析Markdown转换后的HTML
    html = markdown.markdown(md_content)
    soup = BeautifulSoup(html, 'html.parser')

    modified = False

    # 获取md文件中的日期字段
    date_line = ""
    for line in md_content.split('\n'):
        if line.startswith("date:"):
            date_line = line
            break

    md_year_month = ""
    if date_line:
        md_date = date_line.split(":")[1].strip().split("-")
        md_year_month = [str(i).strip('"').strip() for i in md_date[:2]]  # 去除可能存在的空格和引号

    if md_year_month:
        image_folder = os.path.join(base_image_folder, *md_year_month)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        for img_tag in soup.find_all('img'):
            image_url = img_tag['src']
            if image_url.startswith('http'):
                file_name = download_image(image_url, image_folder)
                if file_name:
                    new_src = f'/images/{"/".join(md_year_month)}/{file_name}'  # 图片链接的地址格式
                    md_content = md_content.replace(image_url, new_src)
                    modified = True

    if modified:
        # 如果有修改，则写回文件
        with open(md_path, 'w', encoding='utf-8') as file:
            file.write(md_content)

def process_folder(folder_path):
    """处理指定文件夹中的所有Markdown文件"""
    base_image_folder = os.path.join(folder_path, 'images')
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                update_md_file(md_path, base_image_folder)
                print(f'已处理文件: {md_path}')

# 使用当前工作目录
current_dir = os.getcwd()
process_folder(current_dir)
