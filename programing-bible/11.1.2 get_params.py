# 讀取 URL 參數
import requests

# 將查詢參數定義為字典資料加入 GET 請求中
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('http://httpbin.org/get', params=payload)
print(r) # <Response [200]>