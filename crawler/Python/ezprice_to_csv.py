import html5lib
import requests
from bs4 import BeautifulSoup
import re

import csv

def write_csv_1(items):
    with open('ezprice.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('品項', '價格', '商家'))
        for item in items:
            writer.writerow((column for column in item))

##正式寫入檔案前 先寫入 BOM(Byte Order Mark) 檔案頭 (Windows特有 Mac,Linux可能有相容性問題)
def write_csv_2(items):
    with open('ezprice.csv', 'wb') as f:
        f.write(b'\xEF\xBB\xBF')## 在檔案頭加上utf-8編碼的 BOM
    with open('ezprice.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('品項', '價格', '商家'))
        for item in items:
            writer.writerow((column for column in item))
         
def read_csv():
    with open('ezprice.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['品項'], row['價格'], row['商家'])

query = 'thinkpad'
##文字與數字相加 : TypeError: can only concatenate str (not "int") to str
lowestPrice = 'lp=15000' 
highestPrice = 'hp=60000' 

page = requests.get('https://ezprice.com.tw/s/' + query + '/?' + lowestPrice +'&'+ highestPrice).text
soup = BeautifulSoup(page, 'html5lib')
items = list()

for div in soup.find_all('div', 'search-rst clearfix'):
    item = list()
    item.append(div.h2.a.text.strip()) #商品名稱
    ## 先取得價格字串
    price = div.find('span', 'num').text
    ## 在移除其中非數字部分 (以空白字串取代非0-9的字元)
    price = re.sub(r'[^0-9]', '', price)
    item.append(price)
    ## 若商家區塊存在則取出商家名稱
    if div.find('span', 'platform-name'):
        item.append(div.find('span', 'platform-name').text.strip())
    else:
        item.append('無')
    items.append(item)

print('共 %d 項產品' %(len(items)))

write_csv_1(items)

read_csv()
    

