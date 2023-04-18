# IP 位址查詢器
import requests

# 設定查詢目前 IP 的 api 網址
url = 'https://api.ipify.org'
r = requests.get(url)

print(f'IP 是: {r.text}')