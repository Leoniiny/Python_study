# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import requests, time

items = [
    {
        "id": "2796bfe09e7e4e8abf28e1402a161043",
        "name": "2222",
        "type": 1,
        "robotFlag": 5,
        "questionTypeId": None,
        "parentTypeId": None,
        "questionTypeDesc": None,
        "questionTypeName": None,
        "childTypeList": [
            {
                "id": "ac3fba93835345b8842efbcaf4b5ffe9",
                "name": "二级目录名称",
                "type": 2,
                "robotFlag": None,
                "questionTypeId": "ac3fba93835345b8842efbcaf4b5ffe9",
                "parentTypeId": "-1",
                "questionTypeDesc": None,
                "questionTypeName": "二级目录名称",
                "childTypeList": []
            },
            {
                "id": "9b801adcde8149d2bcb27a9221077a8b",
                "name": "一级目录名称",
                "type": 2,
                "robotFlag": None,
                "questionTypeId": "9b801adcde8149d2bcb27a9221077a8b",
                "parentTypeId": "-1",
                "questionTypeDesc": None,
                "questionTypeName": "一级目录名称",
                "childTypeList": []
            },
            {
                "id": "051dc6a08e524c859fd986a0abead561",
                "name": "编辑目录",
                "type": 2,
                "robotFlag": None,
                "questionTypeId": "051dc6a08e524c859fd986a0abead561",
                "parentTypeId": "-1",
                "questionTypeDesc": None,
                "questionTypeName": "编辑目录",
                "childTypeList": [
                    {
                        "id": "ca1e7ac96a0041c18b50277c4aadf985",
                        "name": "雷洋平",
                        "type": 2,
                        "robotFlag": None,
                        "questionTypeId": "ca1e7ac96a0041c18b50277c4aadf985",
                        "parentTypeId": "051dc6a08e524c859fd986a0abead561",
                        "questionTypeDesc": None,
                        "questionTypeName": "雷洋平",
                        "childTypeList": [
                            {
                                "id": "a20e9ed24ca24748bf6bc203b65e8a9c",
                                "name": "12321",
                                "type": 2,
                                "robotFlag": None,
                                "questionTypeId": "a20e9ed24ca24748bf6bc203b65e8a9c",
                                "parentTypeId": "ca1e7ac96a0041c18b50277c4aadf985",
                                "questionTypeDesc": None,
                                "questionTypeName": "12321",
                                "childTypeList": []
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

finally_list = []


# print(items[0],type(items[0]),sep=r"\n")
def digui(obj):
    for dic_1 in obj:
        finally_list.append(dic_1.get("id"))
        print(f'child_type 的值为{dic_1.get("childTypeList")},类型为：{type(dic_1.get("childTypeList"))}')
        if isinstance(dic_1.get("childTypeList"),list) and len(dic_1.get("childTypeList")) != 0:
            print(f'dic_1 的值为{dic_1}')
            obj = dic_1.get("childTypeList")
            return digui(dic_1.get("childTypeList"))
    # return finally_list

digui(items)
print(finally_list)

