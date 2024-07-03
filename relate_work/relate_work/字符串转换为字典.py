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
    params_str = json.dumps(params_dic)
    # print(f"params_dic  的结果为：{params_str},类型为：{type(params_str)}")
    return params_str


if __name__ == '__main__':
    pass
    str ="sysNum=443af7afa23f4c87a8900f178137d09c&uid=15518753aa88481a90def000599773f0&cid=b448945a058449aca162a24c414f0d73&chooseAdminId=&tranFlag=0&current=false&groupId=&keyword=&keywordId=&queueFlag=&transferType=0&transferAction=&adminHelloWord=%3Cp%3E%E6%82%A8%E5%A5%BD%EF%BC%8C%E8%AF%B7%E9%97%AE%E6%9C%89%E4%BB%80%E4%B9%88%E5%8F%AF%E4%BB%A5%E5%B8%AE%E6%82%A8%E7%9A%84%EF%BC%9F-------%26gt%3B%26gt%3B%E4%BA%BA%E5%B7%A5%E5%AE%A2%E6%9C%8D%E6%AC%A2%E8%BF%8E%E8%AF%AD%3C%2Fp%3E&activeTransfer=1&unknownQuestion=&docId=&answerMsgId=&ruleId=&flowType=&flowCompanyId=&flowGroupId="




    params_str = translate_str_to_dic(str)
    print(params_str)

