# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：解析JSON字符串--商品卡片

import json


'''
cardStyle：样式类型：平铺 :0  列表 :1
cardType：卡片种类：订单:0  商品 :1 
'''
json_str = '''{
	"cardId": "1",
	"cardStyle": "0",
	"cardType": "1",
	"cardTrigger":"0",
	"cardLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
	"customCards": [{
		"customCardName": "索尼WH-100OXM5头戴式智能降噪智能声控蓝牙耳机",
		"customCardThumbnail": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
		"customCardAmount": "10000.00 美元",
		"customCardAmountSymbol":"$",
		"customCardLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
		"customCardDesc": "定制卡片区域字段描述--超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长超长",
		"customMenus": [{
			"menuType": "1",
			"menuName": "自定跳转按钮",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0",
			"menuTip": "按钮提示语"
		},
		{
			"menuType": "2",
			"menuName": "自定发送按钮",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0",
			"menuTip": "按钮提示语"
		}]
		}]
		}'''





data = json.loads(json_str)

# 将JSON数据转换为去掉空格的形式
formatted_json = json.dumps(data, separators=(',', ':'))

# 打印结果
print(formatted_json.encode('utf-8').decode('unicode_escape'))
