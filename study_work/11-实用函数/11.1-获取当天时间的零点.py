# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Fuction：获取当天时间的0点
from datetime import datetime

import arrow
utc = arrow.utcnow()#获取现在的utc时间
local = utc.to('local')#将utc时间转换为本地时间
local_zero = local.replace(hour=0,minute=0,second=0)
local_time  = local_zero.format("YYYY-MM-DD HH:mm:ss")
today_date = local_zero.format("YYYY-MM-DD")
print (local_time)    #输出当天零点时间
print (today_date)    #输出当天日期
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.now().strftime('%Y-%m-%d'))

startDate = None
if startDate is None:
    print(f"startDate  为空，走这里")