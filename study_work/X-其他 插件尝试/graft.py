# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
# 导入json模块
# 导入json模块
import json

data = {
	"pageNo": None,
	"pageCount": None,
	"totalCount": None,
	"pageSize": None,
	"items": [{
		"id": "3b239ef8667d40d8a43be8d92fab3c83",
		"name": "AAAAAAAAAAAAA",
		"type": 1,
		"robotFlag": 5,
		"questionTypeId": None,
		"parentTypeId": None,
		"questionTypeDesc": None,
		"questionTypeName": None,
		"childTypeList": [{
				"id": "c8d3ce48248442f3a3aa2532bf8f4dc1",
				"name": "333",
				"type": 2,
				"robotFlag": None,
				"questionTypeId": "c8d3ce48248442f3a3aa2532bf8f4dc1",
				"parentTypeId": "-1",
				"questionTypeDesc": None,
				"questionTypeName": "333",
				"childTypeList": [{
						"id": "b84bff56e10348c4bbc95461f87cb2a7",
						"name": "333-2",
						"type": 2,
						"robotFlag": None,
						"questionTypeId": "b84bff56e10348c4bbc95461f87cb2a7",
						"parentTypeId": "c8d3ce48248442f3a3aa2532bf8f4dc1",
						"questionTypeDesc": None,
						"questionTypeName": "333-2",
						"childTypeList": []
					},
					{
						"id": "c762909c9af44b0888a0edbe0f763f2e",
						"name": "333-1",
						"type": 2,
						"robotFlag": None,
						"questionTypeId": "c762909c9af44b0888a0edbe0f763f2e",
						"parentTypeId": "c8d3ce48248442f3a3aa2532bf8f4dc1",
						"questionTypeDesc": None,
						"questionTypeName": "333-1",
						"childTypeList": []
					}
				]
			},
			{
				"id": "a9067f447b754402aa477caa82dddcfb",
				"name": "222",
				"type": 2,
				"robotFlag": None,
				"questionTypeId": "a9067f447b754402aa477caa82dddcfb",
				"parentTypeId": "-1",
				"questionTypeDesc": None,
				"questionTypeName": "222",
				"childTypeList": [{
						"id": "6903b9e8fd98492a9065eed640a05388",
						"name": "222-2",
						"type": 2,
						"robotFlag": None,
						"questionTypeId": "6903b9e8fd98492a9065eed640a05388",
						"parentTypeId": "a9067f447b754402aa477caa82dddcfb",
						"questionTypeDesc": None,
						"questionTypeName": "222-2",
						"childTypeList": [{
								"id": "fac1b72cd86e4fa9a71ce519f9a207d8",
								"name": "222-23",
								"type": 2,
								"robotFlag": None,
								"questionTypeId": "fac1b72cd86e4fa9a71ce519f9a207d8",
								"parentTypeId": "6903b9e8fd98492a9065eed640a05388",
								"questionTypeDesc": None,
								"questionTypeName": "222-23",
								"childTypeList": [{
										"id": "f52b971b868e476e98cdd162b03a6240",
										"name": "是多少",
										"type": 2,
										"robotFlag": None,
										"questionTypeId": "f52b971b868e476e98cdd162b03a6240",
										"parentTypeId": "fac1b72cd86e4fa9a71ce519f9a207d8",
										"questionTypeDesc": None,
										"questionTypeName": "是多少",
										"childTypeList": [{
											"id": "ad433acb1483474e961aa926b20eb004",
											"name": "啊方式",
											"type": 2,
											"robotFlag": None,
											"questionTypeId": "ad433acb1483474e961aa926b20eb004",
											"parentTypeId": "f52b971b868e476e98cdd162b03a6240",
											"questionTypeDesc": None,
											"questionTypeName": "啊方式",
											"childTypeList": []
										}]
									},
									{
										"id": "6d0a4538dcb64e6db5e0935a71e81f05",
										"name": "23",
										"type": 2,
										"robotFlag": None,
										"questionTypeId": "6d0a4538dcb64e6db5e0935a71e81f05",
										"parentTypeId": "fac1b72cd86e4fa9a71ce519f9a207d8",
										"questionTypeDesc": None,
										"questionTypeName": "23",
										"childTypeList": []
									},
									{
										"id": "2824c73a5cfc4894806f670bbeca6f31",
										"name": "啊啊发",
										"type": 2,
										"robotFlag": None,
										"questionTypeId": "2824c73a5cfc4894806f670bbeca6f31",
										"parentTypeId": "fac1b72cd86e4fa9a71ce519f9a207d8",
										"questionTypeDesc": None,
										"questionTypeName": "啊啊发",
										"childTypeList": []
									}
								]
							},
							{
								"id": "70eae2945cc548cd8b4eb9dd2fa3df2b",
								"name": "222-22",
								"type": 2,
								"robotFlag": None,
								"questionTypeId": "70eae2945cc548cd8b4eb9dd2fa3df2b",
								"parentTypeId": "6903b9e8fd98492a9065eed640a05388",
								"questionTypeDesc": None,
								"questionTypeName": "222-22",
								"childTypeList": []
							},
							{
								"id": "ed7f14a5dc784269aa3141b431f82b63",
								"name": "222-21",
								"type": 2,
								"robotFlag": None,
								"questionTypeId": "ed7f14a5dc784269aa3141b431f82b63",
								"parentTypeId": "6903b9e8fd98492a9065eed640a05388",
								"questionTypeDesc": None,
								"questionTypeName": "222-21",
								"childTypeList": []
							}
						]
					},
					{
						"id": "55852190b8164b71a7c3d881bcaabe38",
						"name": "222-1",
						"type": 2,
						"robotFlag": None,
						"questionTypeId": "55852190b8164b71a7c3d881bcaabe38",
						"parentTypeId": "a9067f447b754402aa477caa82dddcfb",
						"questionTypeDesc": None,
						"questionTypeName": "222-1",
						"childTypeList": []
					}
				]
			},
			{
				"id": "bdb3f808ae504a67867ab47109b32fdf",
				"name": "111",
				"type": 2,
				"robotFlag": None,
				"questionTypeId": "bdb3f808ae504a67867ab47109b32fdf",
				"parentTypeId": "-1",
				"questionTypeDesc": None,
				"questionTypeName": "111",
				"childTypeList": []
			}
		]
	}],
	"item": None,
	"retCode": "000000",
	"retMsg": "操作成功",
	"zone": None,
	"roleId": None,
	"newConsoleFlag": None,
	"loginCategory": None
}

# 定义一个函数，用递归的方式遍历items数组中的每个字典，并把id添加到数组中
def get_items_id(data, id_list):
    # 如果数据是一个字典，就检查是否有id键
    if isinstance(data, dict):
        # 如果有id键，就把它的值添加到数组中
        if "id" in data:
            id_list.append(data["id"])
        # 对字典中的每个值（可能是列表或字典）调用函数本身
        for value in data.values():
            get_items_id(value, id_list)
    # 如果数据是一个列表，就对它的每个元素（可能是列表或字典）调用函数本身
    elif isinstance(data, list):
        for item in data:
            get_items_id(item, id_list)

# 定义一个空数组，用来存储items数组里的所有id
items_id_list = []


# 调用函数，传入数据中的items数组和空数组
get_items_id(data["items"], items_id_list)

# 打印结果
print(items_id_list)