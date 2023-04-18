# 使用 BeautifulSoup 模組
# pip install -U beautifulsoup4

# 建立 BeautifulSoup 型別物件 sp，解析 「http://www.ehappy.tw/bsdemo1.htm」網頁原始碼。
# 接著用標籤名稱與 text 二個屬性，取出指定的內容。
import requests
from bs4 import BeautifulSoup
url = 'http://www.ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'html.parser')
print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)