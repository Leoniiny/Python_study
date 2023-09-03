# @Time : 2023/2/21 0021 11:35
# @Author : 雷洋平
# @File : faker库使用.py
# @Software: PyCharm
# @Function:
from faker import  Faker

FK = Faker(["zh_CN"])

black_list_name = []
black_list_phone = []
for i in range(10):
    name = FK.name()
    phone = "+86" + str(FK.phone_number())

    black_list_name.append(name)
    black_list_phone.append(phone)
print(black_list_name)
print(black_list_phone,sep="           ")

if __name__ == '__main__':
    dic = {'新增测试1': 161,'新增测试2': 162,'新增测试3': 163}
    # print(list(dic.values()))
    v = dic.get("111")
    # print(v)