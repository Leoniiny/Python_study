# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from datetime import datetime, timedelta
import time


def get_time_stamp(days =6):
    # 获取今天的日期
    today = datetime.now()
    # 最近7天的日期
    before_seven_date = today - timedelta(days=days)
    # 设置时间为当天零点
    before_seven_date = before_seven_date.replace(hour=0, minute=0, second=0, microsecond=0)

    # 设置时间为当天23点59分59秒
    end_of_day = today.replace(hour=23, minute=59, second=59, microsecond=0)

    # 转换为时间戳
    before_seven_date_timestamp = int(before_seven_date.timestamp() * 1000)
    end_of_day_timestamp = int(end_of_day.timestamp() * 1000)
    # 输出结果
    print("最近7天零点的时间戳（毫秒）:", before_seven_date_timestamp)
    print("当天23点59分59秒的时间戳（毫秒）:", end_of_day_timestamp)
    return before_seven_date_timestamp, end_of_day_timestamp
