# 轉換日期格式
# 將 「 - 」為分隔的日期格式做轉換，請設計程式將日期「2017-8-23」轉換為「西元 2017 年 8 月 23 日」。

default_date = '2017-8-23'
default_date = default_date.replace("-", " 年 ", 1)
default_date = default_date.replace("-", " 月 ", 1)

print(f'西元 { default_date } 日')