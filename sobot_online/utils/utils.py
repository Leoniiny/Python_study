# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import os,sys,json
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

import datetime
import time
import hashlib
import base64
import arrow
import random


def get_current_timestamp(digits=13):
    time_stamp = time.time()
    digits = 10 ** (digits - 10)
    time_stamp = int(round(time_stamp * digits))
    return time_stamp


def md5_sign(app_id, currentTime, response_type, app_secret):
    md5sign = hashlib.md5()  # 创建md5对象
    signstring = app_id + str(currentTime) + response_type + app_secret
    md5sign.update(signstring.encode("utf-8"))  # 先对字符串encode,然后进行MD5加密
    md5_value = md5sign.hexdigest()  # hexdigest()为十六进制值，digest()为二进制值
    return md5_value  # 返回md5签名


def base64_secret(pwd: str, companyid: str):
    """
    base64加密原生密码与公司id绑定后的字符串
    @param pwd: 客服自己设置的原生密码
    @param companyid: 公司id
    @return: 加密后的密码
    """
    # 将登陆密码和公司id 链接在一起
    raw_pwd = pwd + companyid
    # 将加密的bytes类型转换为字符串
    base64_encoding = str(base64.b64encode(raw_pwd.encode("utf-8")))
    # 将转换成字符串的base64编码结果截取自己想要的结果
    new_pwd = base64_encoding[2:14]
    # print(new_pwd)
    return new_pwd


def get_today_zero():
    utc = arrow.utcnow()  # 获取现在的utc时间
    local = utc.to('local')  # 将utc时间转换为本地时间
    local_time_zero = local.replace(hour=0, minute=0, second=0)
    now_time = datetime.datetime.now()
    return local_time_zero, now_time

ABS_PATH = os.path.abspath(__file__)  # 获取当前文件的绝对路径
COMMON_PATH = os.path.dirname(ABS_PATH)  # py文件所在的目录
Projection_PATH = os.path.dirname(COMMON_PATH)   # 获取项目的根目录
DATA_PATH = Projection_PATH + r"/data"

if __name__ == '__main__':
    # print(ABS_PATH)
    # print(f"DIR_NAME_  的值为{COMMON_PATH}")
    # print(f"Projection_PATH  的值为{Projection_PATH}")
    # print(f"Projection_PATH  的值为{Projection_PATH + r'''/config_file/operation_config.yml'''}")
    # time1, time2 = get_today_zero()
    # new_time1 = time1.format("YYYY-MM-DD")
    # print(new_time1)
    # print( time2)
    # print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    print(DATA_PATH)
    base64_secret("Lyp123456","443af7afa23f4c87a8900f178137d09c")