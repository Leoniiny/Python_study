# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Fuction：获取时间
import arrow


class GetDate():

    def __init__(self):
        self.utc = arrow.utcnow()  # 获取现在的utc时间对象

    def get_date_format(self, format_num =1, formate ="YYYY-MM-DD",interval_format = None,interval_num = 1):
        if format_num == 2:
            formate = "YYYY-MM-DD HH"
        if format_num == 3:
            formate = "YYYY-MM-DD HH:mm"
        if format_num == 4:
            formate = "YYYY-MM-DD HH:mm:ss"
        if interval_format == "weeks":
            show_time = self.utc.shift(weeks = interval_num).format(f"{formate}")
        elif interval_format == "years":
            show_time = self.utc.shift(years = interval_num).format(f"{formate}")
        elif interval_format == "months":
            show_time = self.utc.shift(months = interval_num).format(f"{formate}")
        else:
            show_time = self.utc.shift(days = interval_num).format(f"{formate}")
        print(f"show_time 的值为：{show_time}")
        return show_time


if __name__ == '__main__':
    obj = GetDate()
    get_date = obj.get_date_format(format_num= 4)

