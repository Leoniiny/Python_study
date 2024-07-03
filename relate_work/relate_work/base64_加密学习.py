# @Time : 2023/2/16 0016 14:48
# @Author : 雷洋平
# @File : base64_加密学习.py
# @Software: PyCharm
# @Function:测试 智齿 登录密码加密方式：base64使用教程：https://blog.csdn.net/xiaokai1999/article/details/128436690
import base64
from base64 import b64encode,b64decode
data_1 = "Lyp123456913d909e3a194598ba61cf904b5dc12a"

raw_base64_encoding = base64.b64encode(data_1.encode("utf-8"))
print(f"raw_base64_encoding 加密结果：{raw_base64_encoding}",type(raw_base64_encoding))

base64_encoding = str(base64.b64encode(data_1.encode("utf-8")))
print(f"base64 加密结果：{base64_encoding}",type(base64_encoding))

# 将转换成字符串的base64编码结果截取自己想要的结果
print(base64_encoding[2:14])

