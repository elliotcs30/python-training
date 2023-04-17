# 讀取 URL 參數
import requests

# 將查詢參數定義為字典資料加入 GET 請求中
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('http://httpbin.org/get', params=payload)
print(r) # <Response [200]>
print(r.text)

'''
{
  "args": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.23.0",
    "X-Amzn-Trace-Id": "Root=1-643d1112-57a6e45f2ff3d2d00fd76e69"
  },
  "origin": "210.63.211.145",
  "url": "http://httpbin.org/get?key1=value1&key2=value2"
}
'''