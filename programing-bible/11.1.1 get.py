# 安裝 requests 模組
# pip install -U requests

# requests 模組可以不透過瀏覽器就能完成 GET 的請求
# import requests
# Response 物件 = requests.get(網址)

# 讀取網頁原始碼
import requests
url = 'http://www.ehappy.tw/demo.htm'
r = requests.get(url)

# 檢查 HTTP 回應碼是否為 200 （requests.code.ok）
if r.status_code == requests.codes.ok:
    print(r.text)