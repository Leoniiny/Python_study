# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from faker import Faker

fake = Faker(locale="zh_CN")
# i =1
# while True:
#     if i < 10:
#         i += 1
#         print(i)
#     else:
#         print(fake.paragraph())
#         print(fake.sentences())
#         # print(len(['96ee4e7487e94a60b3fec51ef7f78422', '95a38dfc34bb4b1ca5c6a57a34eb7a2a', '56449f57ced4441086429ddc0200ef0c', '637a923e5264441393a3aa84b9404a05', '697dc0d117904611a08b727a901ce347', '79bc2cb079fa48ffb72802628c7cabc2', '88e871f3a2004410be912d97c38689c4', '425ea3f7e33941deb50abb7b7b3a587c', 'd3b70435f57947cb9555be99c478b383', '92b80f604e544f09b209329e74be8d9f', '9427c7e7dc164b069fd680abbcb12b66', 'b22b75ae00b1401898a3bd4d98d61204', 'f4b498a437a74486911ba9b1c79ed9aa', 'fdb510d098dd45899f93778d2b06fa72', '0be515ff56714c52ae3d81e65127428b', '29967139e63846ef858dda32e6c55c56', '926bd56ef50f4d6e809989e131fa64d5', 'a226891558694a0eb61611197825ed93', 'b43fc89f046341a0b29fc33db81e7de5', '1dd74c9858574f569dec01e5b0450296', '03ae6c665a7e4a649fd6d571f1626296', '68dee0689c4e41e2a7c738f89e772b2f', 'de2be083a57c4ca6b177783b0411d39c', '94c0200f9d744d4baa129f2bfa5871fa', 'cca7683f5a9c4b4ab255a0b86eaa9eec']))
#         break

data = {
    "items": [{
        "companyId": "150d6fa1252f482094b708f2b19a1bb1",
        "createId": "",
        "createTime": 1650852636572,
        "departId": "e368cc6e85b84378b6d5fc81aefe0eb6",
        "departLevel": 0,
        "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6",
        "departName": "总公司",
        "departType": "1,2,3,4",
        "parentId": "0",
        "subDepartmentList": [{
            "companyId": "150d6fa1252f482094b708f2b19a1bb1",
            "createId": "2aad70f092e44e1fb754b6286bd3adf8",
            "createTime": 1652259533692,
            "departId": "2ab9cde08ef0400a9c3a3a265992d02e",
            "departLevel": 1,
            "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|2ab9cde08ef0400a9c3a3a265992d02e",
            "departName": "在线客服部",
            "departType": "1,2,3,4",
            "parentId": "e368cc6e85b84378b6d5fc81aefe0eb6",
            "sourceNo": 1,
            "subDepartmentList": [{
                "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                "createTime": 1652259886521,
                "departId": "cc64576bacf54f3d8be3f640ba18c446",
                "departLevel": 2,
                "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|2ab9cde08ef0400a9c3a3a265992d02e|cc64576bacf54f3d8be3f640ba18c446",
                "departName": "在线客服一分部",
                "departType": "1,2,3,4",
                "parentId": "2ab9cde08ef0400a9c3a3a265992d02e",
                "sourceNo": 1,
                "subFlag": 0
            }, {
                "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                "createTime": 1652259906127,
                "departId": "733368ea41034c33a684029c384d8e32",
                "departLevel": 2,
                "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|2ab9cde08ef0400a9c3a3a265992d02e|733368ea41034c33a684029c384d8e32",
                "departName": "在线客服二分部",
                "departType": "1,2,3,4",
                "parentId": "2ab9cde08ef0400a9c3a3a265992d02e",
                "sourceNo": 2,
                "subFlag": 0
            }],
            "subFlag": 1,
            "updateId": "2aad70f092e44e1fb754b6286bd3adf8",
            "updateTime": 1652259892787
        }, {
            "companyId": "150d6fa1252f482094b708f2b19a1bb1",
            "createId": "2aad70f092e44e1fb754b6286bd3adf8",
            "createTime": 1656485026566,
            "departId": "eca6347d113f4fb7863a89169e438d08",
            "departLevel": 1,
            "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|eca6347d113f4fb7863a89169e438d08",
            "departName": "客服处于多部门测试",
            "departType": "1,4",
            "parentId": "e368cc6e85b84378b6d5fc81aefe0eb6",
            "sourceNo": 1,
            "subDepartmentList": [{
                "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                "createTime": 1656485039371,
                "departId": "b5847fc86b1c4c169f81ab9eab3abb91",
                "departLevel": 2,
                "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|eca6347d113f4fb7863a89169e438d08|b5847fc86b1c4c169f81ab9eab3abb91",
                "departName": "测试1",
                "departType": "1",
                "parentId": "eca6347d113f4fb7863a89169e438d08",
                "sourceNo": 1,
                "subFlag": 0
            }],
            "subFlag": 1
        }, {
            "companyId": "150d6fa1252f482094b708f2b19a1bb1",
            "createId": "2aad70f092e44e1fb754b6286bd3adf8",
            "createTime": 1654762635749,
            "departId": "df3f40dd3f774eb3bd42e3d6f0172629",
            "departLevel": 1,
            "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629",
            "departName": "西南电销分部",
            "departType": "1,2,3,4",
            "parentId": "e368cc6e85b84378b6d5fc81aefe0eb6",
            "sourceNo": 2,
            "subDepartmentList": [{
                "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                "createTime": 1654762650817,
                "departId": "d011631ca54e43caaffe2bb55daa050d",
                "departLevel": 2,
                "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|d011631ca54e43caaffe2bb55daa050d",
                "departName": "西南电销分部-01",
                "departType": "1,2,3,4",
                "parentId": "df3f40dd3f774eb3bd42e3d6f0172629",
                "sourceNo": 1,
                "subFlag": 0
            }, {
                "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                "createTime": 1654762657488,
                "departId": "69bfce1b68154188a11eaba3607a7e9c",
                "departLevel": 2,
                "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c",
                "departName": "西南电销分部-02",
                "departType": "1,2,3,4",
                "parentId": "df3f40dd3f774eb3bd42e3d6f0172629",
                "sourceNo": 2,
                "subDepartmentList": [{
                    "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                    "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                    "createTime": 1654762680665,
                    "departId": "1c9acc1beb69438f8c8dca7f0ca8eafc",
                    "departLevel": 3,
                    "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|1c9acc1beb69438f8c8dca7f0ca8eafc",
                    "departName": "西南电销2分部-01",
                    "departType": "1,2,3,4",
                    "parentId": "69bfce1b68154188a11eaba3607a7e9c",
                    "sourceNo": 1,
                    "subDepartmentList": [{
                        "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                        "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                        "createTime": 1654762720605,
                        "departId": "ab1058471c90462eaeb770881cccf9b4",
                        "departLevel": 4,
                        "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|1c9acc1beb69438f8c8dca7f0ca8eafc|ab1058471c90462eaeb770881cccf9b4",
                        "departName": "西南电销分部-011",
                        "departType": "1,2,3,4",
                        "parentId": "1c9acc1beb69438f8c8dca7f0ca8eafc",
                        "sourceNo": 1,
                        "subFlag": 0
                    }, {
                        "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                        "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                        "createTime": 1654762728292,
                        "departId": "4a0e83b69ec14f758f28959286bc4998",
                        "departLevel": 4,
                        "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|1c9acc1beb69438f8c8dca7f0ca8eafc|4a0e83b69ec14f758f28959286bc4998",
                        "departName": "西南电销分部-012",
                        "departType": "1,2,3,4",
                        "parentId": "1c9acc1beb69438f8c8dca7f0ca8eafc",
                        "sourceNo": 2,
                        "subFlag": 0
                    }],
                    "subFlag": 1,
                    "updateId": "2aad70f092e44e1fb754b6286bd3adf8",
                    "updateTime": 1654762704269
                }, {
                    "companyId": "150d6fa1252f482094b708f2b19a1bb1",
                    "createId": "2aad70f092e44e1fb754b6286bd3adf8",
                    "createTime": 1654762694312,
                    "departId": "6cfda13fd2cb4207801ddf3dcdf972ee",
                    "departLevel": 3,
                    "departLevelNo": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|6cfda13fd2cb4207801ddf3dcdf972ee",
                    "departName": "西南电销2分部-02",
                    "departType": "1,2,3,4",
                    "parentId": "69bfce1b68154188a11eaba3607a7e9c",
                    "sourceNo": 2,
                    "subFlag": 0
                }],
                "subFlag": 1
            }],
            "subFlag": 1
        }],
        "subFlag": 1
    }],
    "retCode": "000000"
}

# 定义一个空数组，用来存放所有的id
ids = []


# 定义一个递归函数，接收一个items数组作为参数
def get_ids(items):
    # 遍历items数组中的每个元素
    for item in items:
        # 将元素的id添加到ids数组中
        ids.append(item["departId"])
        # 如果元素有subDepartmentList属性，且subDepartmentList不为空
        if "subDepartmentList" in item and item["subDepartmentList"]:
            # 对subDepartmentList进行递归调用
            get_ids(item["subDepartmentList"])


# 调用递归函数，传入原始的items数组
get_ids(data["items"])

# 打印ids数组
print(ids, len(ids), sep="===>>>>:")
