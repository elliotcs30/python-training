# 列印時間函式所有資訊
# 大賽看板上需顯示以中華民國年份表示的現在時刻，給比賽選手做為參考。
# 請設計程式以時間模組列印以中華民國年份表示的現在時刻及節約時間資訊。

import time as t

week = ["一", "二", "三", "四", "五", "六", "日"]
dst = ["無日光節約時間", "有日光節約時間"]
local_time = t.localtime()

show = f"現在時刻: 中華民國 {str(int(local_time.tm_year)-1911)} 年 \
{str(int(local_time.tm_mon))} 月 \
{str(int(local_time.tm_mday))} 日 \
{str(int(local_time.tm_hour))} 點 \
{str(int(local_time.tm_min))} 分 \
{str(int(local_time.tm_sec))} 秒 \
星期 {week[local_time.tm_wday]} \
今天是今年的第 {str(int(local_time.tm_yday))} 天，此地 {dst[local_time.tm_isdst]}"

print(show) # 現在時刻: 中華民國 112 年 4 月 11 日 14 點 11 分 37 秒 星期 二 今天是今年的第 101 天，此地 無日光節約時間