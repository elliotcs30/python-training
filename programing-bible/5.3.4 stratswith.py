# 檢查網址格式
# 程式設計讓使用者輸入網址，程式會檢查輸入的網址格式是否正確。

url = input('請輸入網址:')

if (url.startswith('http://')) or (url.startswith('https://')):
    print('輸入的網址格式正確！')
else:
    print('輸入的網址格式錯誤！')