import html5lib
import requests
from bs4 import BeautifulSoup
import re

resp = requests.get('https://www.ptwxz.com/html/7/7580/')
##設置查詢網頁編碼 預設為utf-8?
resp.encoding = 'gbk'
soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.find('div', 'title').text.strip()
contents = list()

print('title :', title)
for charpter in soup.find_all('a', {'href': re.compile('[0-9]+.html')}):
    contents.append(charpter.text.strip())
    print('charpter :',charpter.text.strip())

with open(title + '.txt', 'w', encoding='utf-8') as f:
    for content in contents:
            f.write(content)
            f.write('\n')