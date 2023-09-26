# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import json
import re
data ={
    "pageNo": None,
    "pageCount": None,
    "totalCount": None,
    "pageSize": None,
    "items": [
        {
            "id": "55ddbff25da94656a6efde6d09fc0a5c",
            "name": "Holy See (Vatican City State)",
            "type": 1,
            "robotFlag": 23,
            "questionTypeId": None,
            "parentTypeId": None,
            "questionTypeDesc": None,
            "questionTypeName": None,
            "childTypeList": [
                {
                    "id": "5366c57b95034d87b823b054544d3d9a",
                    "name": "12",
                    "type": 2,
                    "robotFlag": None,
                    "questionTypeId": "5366c57b95034d87b823b054544d3d9a",
                    "parentTypeId": "-1",
                    "questionTypeDesc": None,
                    "questionTypeName": "12",
                    "childTypeList": [
                        {
                            "id": "5c6726c10d5f4c13aef5c407d1592eca",
                            "name": "robotFlag收到发斯蒂芬",
                            "type": 2,
                            "robotFlag": None,
                            "questionTypeId": "5c6726c10d5f4c13aef5c407d1592eca",
                            "parentTypeId": "5366c57b95034d87b823b054544d3d9a",
                            "questionTypeDesc": None,
                            "questionTypeName": "robotFlag收到发斯蒂芬",
                            "childTypeList": []
                        },
                        {
                            "id": "241c9268ed8a41d28136ba46236d2d7d",
                            "name": "34erqw",
                            "type": 2,
                            "robotFlag": None,
                            "questionTypeId": "241c9268ed8a41d28136ba46236d2d7d",
                            "parentTypeId": "5366c57b95034d87b823b054544d3d9a",
                            "questionTypeDesc": None,
                            "questionTypeName": "34erqw",
                            "childTypeList": []
                        }
                    ]
                },
                {
                    "id": "c0c5ade78eff4bcca5f0ddce089bd5a9",
                    "name": "11",
                    "type": 2,
                    "robotFlag": None,
                    "questionTypeId": "c0c5ade78eff4bcca5f0ddce089bd5a9",
                    "parentTypeId": "-1",
                    "questionTypeDesc": None,
                    "questionTypeName": "11",
                    "childTypeList": [
                        {
                            "id": "ba7cd24983a4401c8e8d176fd1b91d52",
                            "name": "阿斯顿发顺丰撒",
                            "type": 2,
                            "robotFlag": None,
                            "questionTypeId": "ba7cd24983a4401c8e8d176fd1b91d52",
                            "parentTypeId": "c0c5ade78eff4bcca5f0ddce089bd5a9",
                            "questionTypeDesc": None,
                            "questionTypeName": "阿斯顿发顺丰撒",
                            "childTypeList": [
                                {
                                    "id": "a0b063a6b44247158087fa819f935017",
                                    "name": "但是风格梵蒂冈",
                                    "type": 2,
                                    "robotFlag": None,
                                    "questionTypeId": "a0b063a6b44247158087fa819f935017",
                                    "parentTypeId": "ba7cd24983a4401c8e8d176fd1b91d52",
                                    "questionTypeDesc": None,
                                    "questionTypeName": "但是风格梵蒂冈",
                                    "childTypeList": []
                                },
                                {
                                    "id": "9eeac4f144ee4bf8b5cb8cfd773fe17a",
                                    "name": "撒旦法发生的",
                                    "type": 2,
                                    "robotFlag": None,
                                    "questionTypeId": "9eeac4f144ee4bf8b5cb8cfd773fe17a",
                                    "parentTypeId": "ba7cd24983a4401c8e8d176fd1b91d52",
                                    "questionTypeDesc": None,
                                    "questionTypeName": "撒旦法发生的",
                                    "childTypeList": []
                                }
                            ]
                        },
                        {
                            "id": "1e2c70c46a4e49afb333696194944cbe",
                            "name": "发生发撒答复",
                            "type": 2,
                            "robotFlag": None,
                            "questionTypeId": "1e2c70c46a4e49afb333696194944cbe",
                            "parentTypeId": "c0c5ade78eff4bcca5f0ddce089bd5a9",
                            "questionTypeDesc": None,
                            "questionTypeName": "发生发撒答复",
                            "childTypeList": [
                                {
                                    "id": "70182c1310e04166b06e88368674f674",
                                    "name": "法师打发",
                                    "type": 2,
                                    "robotFlag": None,
                                    "questionTypeId": "70182c1310e04166b06e88368674f674",
                                    "parentTypeId": "1e2c70c46a4e49afb333696194944cbe",
                                    "questionTypeDesc": None,
                                    "questionTypeName": "法师打发",
                                    "childTypeList": []
                                },
                                {
                                    "id": "59213fc62cd44bab9e9f724f8faeca67",
                                    "name": "阿斯顿发斯蒂芬",
                                    "type": 2,
                                    "robotFlag": None,
                                    "questionTypeId": "59213fc62cd44bab9e9f724f8faeca67",
                                    "parentTypeId": "1e2c70c46a4e49afb333696194944cbe",
                                    "questionTypeDesc": None,
                                    "questionTypeName": "阿斯顿发斯蒂芬",
                                    "childTypeList": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "8d1ceadcbb874b4bb4418e5b5737e85e",
                    "name": "",
                    "type": 2,
                    "robotFlag": None,
                    "questionTypeId": "8d1ceadcbb874b4bb4418e5b5737e85e",
                    "parentTypeId": "-1",
                    "questionTypeDesc": None,
                    "questionTypeName": "",
                    "childTypeList": []
                }
            ]
        }
    ],
    "item": None,
    "retCode": "000000",
    "retMsg": "操作成功",
    "zone": None,
    "roleId": None,
    "newConsoleFlag": None,
    "loginCategory": None
}

new_list = re.findall(r'"questionTypeId": "(.*?)","parentTypeId": "-1"',json.dumps(data))
print(new_list)