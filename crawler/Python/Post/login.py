import requests
from bs4 import BeautifulSoup

URL = 'LoginWebAddress'

## 創建 Session 物件
s = requests.Session()

## 先瀏覽網頁, 取得 crsf token
resp = s.get(URL)
soup = BeautifulSoup(resp.text, 'html5lib')
crsf = soup.find('form', id='ajax-login').find('input', 'crsftok')['value']

##傳送表單資料並登入 依照 Form Data 傳送資料建立, 此範例為: crsftok, email, password
form_data = {
    'email': 'YourAccount',
    'password': 'YourPassword',
    'crsftok': crsf
}

resp = s.post(URL, data=form_data)

## 登入成功後, 相關資訊皆保留在 session 物件中, 可以直接索取相關網頁資訊
resp = s.get('UserInfoWebAddress')

print(resp.text)