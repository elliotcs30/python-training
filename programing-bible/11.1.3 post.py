# 發送 post 請求
import requests

# 將查詢參數加入 POST 請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.28.2", 
    "X-Amzn-Trace-Id": "Root=1-643d561d-549f202527eebe0e08659e8f"
  }, 
  "json": null, 
  "origin": "IP", 
  "url": "http://httpbin.org/post"
}
'''