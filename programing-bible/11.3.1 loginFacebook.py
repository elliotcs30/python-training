# 實戰 Facebook 自動登入

# 安裝 Selenium 模組
# pip install selenium

# 下載 Chrome WebDriver
# https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver

# 設定 facebook 登入資訊
url = 'https://www.facebook.com/'
email = 'email@gamil.com'
password = 'password'

# 建立瀏覽器物件
driver = webdriver.Chrome()

# 最大化視窗後開啟 facebook 網站
driver.maximize_window()
driver.get(url)

# 執行自動登入動作
driver.find_element_by_id('email').send_keys(email) # 輸入郵件
driver.find_element_by_id('pass').send_keys(password) # 輸入密碼
driver.find_element_by_name('login').click()