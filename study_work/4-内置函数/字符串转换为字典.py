# @Time : 2023/3/20 0020 16:33
# @Author : 雷洋平
# @File : 字符串转换为字典.py
# @Software: PyCharm
# @Function:字符串转换为字典
import json


def translate_str_to_dic(string: str):
    str_list = string.split("&")
    params_dic = {}
    # print(f"str 的结果为{str_list}")
    for temp_str in str_list:
        temp_list = temp_str.split("=")
        params_dic[temp_list[0]] = temp_list[-1]
    # print(f"params_dic  的结果为：{params_dic}")
    params_str = json.dumps(params_dic)
    # print(f"params_dic  的结果为：{params_str},类型为：{type(params_str)}")
    return params_str


if __name__ == '__main__':
    pass
    str = ""
    params_str = translate_str_to_dic(str)
    print(params_str)

