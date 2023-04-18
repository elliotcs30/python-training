# 爬取 PTT 在請求時加入「over18 = 1」的 cookie 值。
import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# 設定 cookie 的值
cookies = {'over18' : '1'}
r = requests.get(url, cookies = cookies)
print(r.text) # 顯示目標網頁內容