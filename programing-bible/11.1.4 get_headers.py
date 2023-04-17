# 台灣高鐵的網路訂票頁面，當進行 HTTP 要求時會先檢查操作者是否為瀏覽器，如果不是則無法正常讀取內容。
# 利用自訂 HTTP Headers 的方式偽裝為瀏覽器的操作，跳過檢查進入網站。
import requests
url = 'https://irs.thsrc.com.tw/IMINT'

# 自訂標頭
headers = {
    'user-agent':'Mozilla/5.0(Windows NT 10.0; win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

# 將自訂表頭加入 GET 請求中
r = requests.get(url, headers=headers)
print(r)