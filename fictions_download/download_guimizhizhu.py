#!/usr/bin/env python3
__author__ = 'zhangyangrong'

import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    server = 'https://www.vbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.vbiquge.com/15_15338/'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    #用BS解析
    chapter_bs = BeautifulSoup(html, 'lxml')

    #章节名
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')

    #tqdm模块是python进度条库
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')