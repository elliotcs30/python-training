import datetime
from dateutil.relativedelta import relativedelta

# 當前日期時間
print(datetime.datetime.now()) # 2023-04-11 03:10:48.908041

# 格式化時間
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) # 2023-04-11 03:10

# 日期加一天
print((datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")) # 2023-04-12 03:20:24

# 日期減一天
print((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")) # 2023-04-10 03:39:52

# 提前 1 小時 / 提前 1　分鐘
print((datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")) # 2023-04-11 04:39:52

# 提前 1 年
now = datetime.datetime.now()
print((now+relativedelta(years=1)).strftime("%Y-%m-%d %H:%M:%S"))
