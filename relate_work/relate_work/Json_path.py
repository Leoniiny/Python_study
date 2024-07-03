import json
from jsonpath import jsonpath
# Python 字典类型转换为 JSON 对象
data = {"items":[{"group_name":"超管分组2","group_type":"1","groupid":"d43e033887c141318cd6236afad53d45"},
                 {"group_name":"超管分组3","group_type":"1","groupid":"9ffc4b479f9c4cf1b5c4a728c70e5d7e"},
                 {"group_name":"超管组","group_type":"1","groupid":"7c52b375120a4c9599cf046f2742afdc"},
                 {"group_name":"管理员组","group_type":"1","groupid":"22ddc33c03ef45ac80eb55fa63127dcc"},
                 {"group_name":"全部管理员可见1","group_type":"1","groupid":"40be4bc71947458abb81d458bad07702"},
                 {"group_name":"全部管理员可见2","group_type":"1","groupid":"53dbf9d056464ac3a53dd5af564d62e9"},
                 {"group_name":"全渠道分组-1","group_type":"1","groupid":"2c3d5e36c3ed4d4bbfac3be95542cdc1"},
                 {"group_name":"全渠道分组-2","group_type":"1","groupid":"6577d256a4ed45abb422d90f15a0c9e1"},
                 {"group_name":"在线技能组1656054953632","group_type":"1","groupid":"1e001c4aafe649e4a59536f3d1706626"},
                 {"group_name":"在线技能组1656054974991","group_type":"1","groupid":"514bc221fbbd4a319e8d0d62b6a6856f"},
                 {"group_name":"在线技能组1656054975187","group_type":"1","groupid":"4aa72d0d25f74b57841785b26bac8f91"},
                 {"group_name":"在线技能组1656054975358","group_type":"1","groupid":"9983136cd3314a48865fcf5531de9636"},
                 {"group_name":"在线技能组1656054975515","group_type":"1","groupid":"dbf2393343f04e429799bae5278f3079"},
                 {"group_name":"在线技能组1656054976070","group_type":"1","groupid":"e753250a08e047e795fd7ded22b11efc"},
                 {"group_name":"在线技能组1656054976253","group_type":"1","groupid":"dfbf1908075f441891e0ef1bf7624318"}],
        "page_count":3,
        "page_no":1,
        "page_size":15,
        "ret_code":"000000",
        "ret_msg":"操作成功",
        "total_count":42}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))   #repr() 函数将对象转化为供解释器读取的形式。
print("JSON 对象：", json_str)
# jsonpath 需要将json字符串转换为字典，才能进行调用
list1 = jsonpath(data,"$.items")
print(list1)