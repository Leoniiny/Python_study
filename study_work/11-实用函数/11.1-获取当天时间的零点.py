# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Fuction：获取当天时间的0点
from datetime import datetime

import arrow

utc = arrow.utcnow()  # 获取现在的utc时间对象
test_yesterday = utc.shift(days=-1).format("YYYY-MM-DD HH")
print(f"test_yesterday  的值为：{test_yesterday}")

local_obj = utc.to('local')  # 将utc时间转换为本地时间
local_zero = local_obj.replace(hour=0, minute=0, second=0)
local_time = local_zero.format("YYYY-MM-DD HH:mm:ss")
today_date = local_zero.format("YYYY-MM-DD")
yesterday = local_zero.shift(days=-1).format("YYYY-MM-DD")
print(f"yesterday  的值为：{yesterday}")

tendays_after = local_zero.shift(days=10).format("YYYY-MM-DD HH:mm")
print(f"tendays_after  的值为：{tendays_after}")





print(local_time)  # 输出当天零点时间
print(today_date)  # 输出当天日期
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
today_date01 = datetime.now().strftime('%Y-%m-%d')
today_date02 = datetime.now().strftime('%Y-%m-%d %H')
print(today_date01)
print(f"today_date02  的值为：{today_date02}")

startDate = None
if startDate is None:
    print(f"startDate  为空，走这里")
