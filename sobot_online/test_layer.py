# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：

import requests
from bs4 import BeautifulSoup

def get_sz300_info():
    url = "http://quote.eastmoney.com/sh600519.html"  # 沪深300指数的URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找涨跌数和涨跌率
        change = soup.find('div', class_='zs').find_all('span')[1].text  # 涨跌数
        change_rate = soup.find('div', class_='zs').find_all('span')[2].text  # 涨跌率

        return change, change_rate
    else:
        print("Failed to retrieve data")
        return None, None

change, change_rate = get_sz300_info()
if change and change_rate:
    print(f"沪深300指数涨跌数: {change}")
    print(f"沪深300指数涨跌率: {change_rate}")

