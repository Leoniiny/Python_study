# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import requests, time



# 在这里输入你的 JSON 数据
json_data = {
        "items": [
            {
                "departLevel": 0,
                "departType": "1,2,3,4",
                "disabled": True,
                "id": "e368cc6e85b84378b6d5fc81aefe0eb6",
                "name": "总公司",
                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6",
                "subList": [
                    {
                        "departLevel": 1,
                        "departType": "1,2,3,4",
                        "disabled": True,
                        "id": "2ab9cde08ef0400a9c3a3a265992d02e",
                        "name": "在线客服部",
                        "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|2ab9cde08ef0400a9c3a3a265992d02e",
                        "subList": [
                            {
                                "departLevel": 2,
                                "departType": "1,2,3,4",
                                "disabled": True,
                                "id": "733368ea41034c33a684029c384d8e32",
                                "name": "在线客服二分部",
                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|2ab9cde08ef0400a9c3a3a265992d02e|733368ea41034c33a684029c384d8e32",
                                "subList": []
                            },
                            {
                                "departLevel": 2,
                                "departType": "1,2,3,4",
                                "disabled": True,
                                "id": "cc64576bacf54f3d8be3f640ba18c446",
                                "name": "在线客服一分部",
                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|2ab9cde08ef0400a9c3a3a265992d02e|cc64576bacf54f3d8be3f640ba18c446",
                                "subList": []
                            }
                        ]
                    },
                    {
                        "departLevel": 1,
                        "departType": "1,2,3,4",
                        "disabled": True,
                        "id": "df3f40dd3f774eb3bd42e3d6f0172629",
                        "name": "西南电销分部",
                        "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629",
                        "subList": [
                            {
                                "departLevel": 2,
                                "departType": "1,2,3,4",
                                "disabled": True,
                                "id": "69bfce1b68154188a11eaba3607a7e9c",
                                "name": "西南电销分部-02",
                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c",
                                "subList": [
                                    {
                                        "departLevel": 3,
                                        "departType": "1,2,3,4",
                                        "disabled": True,
                                        "id": "1c9acc1beb69438f8c8dca7f0ca8eafc",
                                        "name": "西南电销2分部-01",
                                        "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|1c9acc1beb69438f8c8dca7f0ca8eafc",
                                        "subList": [
                                            {
                                                "departLevel": 4,
                                                "departType": "1,2,3,4",
                                                "disabled": True,
                                                "id": "4a0e83b69ec14f758f28959286bc4998",
                                                "name": "西南电销分部-012",
                                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|1c9acc1beb69438f8c8dca7f0ca8eafc|4a0e83b69ec14f758f28959286bc4998",
                                                "subList": []
                                            },
                                            {
                                                "departLevel": 4,
                                                "departType": "1,2,3,4",
                                                "disabled": True,
                                                "id": "ab1058471c90462eaeb770881cccf9b4",
                                                "name": "西南电销分部-011",
                                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|1c9acc1beb69438f8c8dca7f0ca8eafc|ab1058471c90462eaeb770881cccf9b4",
                                                "subList": []
                                            }
                                        ]
                                    },
                                    {
                                        "departLevel": 3,
                                        "departType": "1,2,3,4",
                                        "disabled": True,
                                        "id": "6cfda13fd2cb4207801ddf3dcdf972ee",
                                        "name": "西南电销2分部-02",
                                        "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|69bfce1b68154188a11eaba3607a7e9c|6cfda13fd2cb4207801ddf3dcdf972ee",
                                        "subList": []
                                    }
                                ]
                            },
                            {
                                "departLevel": 2,
                                "departType": "1,2,3,4",
                                "disabled": True,
                                "id": "d011631ca54e43caaffe2bb55daa050d",
                                "name": "西南电销分部-01",
                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|df3f40dd3f774eb3bd42e3d6f0172629|d011631ca54e43caaffe2bb55daa050d",
                                "subList": []
                            }
                        ]
                    },
                    {
                        "departLevel": 1,
                        "departType": "1,4",
                        "disabled": True,
                        "id": "eca6347d113f4fb7863a89169e438d08",
                        "name": "客服处于多部门测试",
                        "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|eca6347d113f4fb7863a89169e438d08",
                        "subList": [
                            {
                                "departLevel": 2,
                                "departType": "1",
                                "disabled": True,
                                "id": "b5847fc86b1c4c169f81ab9eab3abb91",
                                "name": "测试1",
                                "path": "150d6fa1252f482094b708f2b19a1bb1|e368cc6e85b84378b6d5fc81aefe0eb6|eca6347d113f4fb7863a89169e438d08|b5847fc86b1c4c169f81ab9eab3abb91",
                                "subList": []
                            }
                        ]
                    }
                ]
            }
        ],
        "retCode": "000000",
        "retMsg": "操作成功"
    }

def extract_all_ids(data):
    ids = []

    if isinstance(data, dict):
        if "id" in data:
            ids.append(data["id"])
        for key, value in data.items():
            ids.extend(extract_all_ids(value))
    elif isinstance(data, list):
        for item in data:
            ids.extend(extract_all_ids(item))

    return ids


items = json_data.get("items", [])
all_ids = extract_all_ids(items)

print("All IDs:", all_ids)
