# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：订单卡片设置
import json


'''
cardStyle：样式类型：平铺 :0  列表 :1
cardType：卡片种类：订单:0  商品 :1 
'''

json_str = '''
{
	"cardId": "1",
	"cardStyle": "1",
	"cardType": "1",
	"cardTrigger":"0",
	"cardGuide": "1234567890123567890123456789012345678901234567890",
	"cardImg": "https://img.sobot.com/chatres/137647808eba49b8ab81b4cf0b8e8c9d/msg/20230628/4eef15f80e3a8e25448365cef0d31b0f/aece05e116d24ac99ced073e5ed95eed.png",
	"cardDesc": "通用卡片-超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述",
	"customField": {
		"自定义字段1": "自定义字段1",
		"自定义字段2": "自定义字段2",
		"自定义字段3": "自定义字段3",
		"自定义字段4": "自定义字段4",
		"自定义字段5": "自定义字段5",
		"自定义字段6": "自定义字段6",
		"自定义字段7": "自定义字段7",
		"自定义字段8": "自定义字段8",
		"自定义字段9": "自定义字段9",
		"自定义字段10": "自定义字段10"
	},
	"cardLink": "https://img.sobot.com/chatres/137647808eba49b8ab81b4cf0b8e8c9d/msg/20230628/4eef15f80e3a8e25448365cef0d31b0f/aece05e116d24ac99ced073e5ed95eed.png",
	"customCards": [
{
		"customCardStatus": "发货中",
		"customCardCount": "商品共：1件",
		"customCardCode": "10611111",
		"customCardTime": "2023-06-20 18:22:17",
		"customCardId": "10611111",
		"customCardName": "索尼WH-100OXM5头戴式智能降噪智能声控蓝牙耳机",
		"customCardThumbnail": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
		"customCardAmount": "699000.00",
"customCardAmountSymbol":"￥",
		"customCardLink": "https://img.sobot.com/chatres/137647808eba49b8ab81b4cf0b8e8c9d/msg/20230628/4eef15f80e3a8e25448365cef0d31b0f/9077696f25094b73a096a1d7db81ebe7.png",
		"customCardDesc": "自定义卡片-超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述",
		"customMenus": [{
			"menuType": 2,
			"menuName": "第2发送按钮",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0"
		}, {
			"menuType": 0,
			"menuName": "第2跳转",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "1",
			"menuTip": "按钮提示语"
		}, {
			"menuType": 1,
			"menuName": "确认",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0",
			"menuTip": "第二件商品的确认按钮提示语"
		}]
	},
{
		"customCardStatus": "已付款",
		"customCardCount": "2件",
		"customCardCode": "10611111",
		"customCardTime": "2023-06-20 18:22:17",
		"customCardId": "10611111",
		"customCardName": "索尼WH-100OXM5头戴式智能降噪智能声控蓝牙耳机",
		"customCardThumbnail": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
		"customCardAmount": "999000.00",
"customCardAmountSymbol":"￥",
		"customCardLink": "https://img.sobot.com/chatres/137647808eba49b8ab81b4cf0b8e8c9d/msg/20230628/4eef15f80e3a8e25448365cef0d31b0f/9077696f25094b73a096a1d7db81ebe7.png",
		"customCardDesc": "自定义卡片-超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述超长描述",
		"customMenus": [{
			"menuType": 0,
			"menuName": "第3跳转",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0",
			"menuTip": "按钮提示语"
		},
		 {
			"menuType": 2,
			"menuName": "第3发送按钮",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0"
		}, {
			"menuType": 1,
			"menuName": "确认",
			"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
			"menuLinkType": "0",
			"menuTip": "按钮提示语"
		}]
	}],
	"cardMenus": [{
		"menuType": "0",
		"menuName": "通用卡片跳转按钮",
		"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
		"menuLinkType": "1",
		"menuTip": "按钮提示语"
	}, {
		"menuType": "2",
		"menuName": "通用卡片发送按钮",
		"menuLink": "http://img3.sobot.com/chatres/a6c9535d3bbf48e7b7c7d5ea3533fcf3/msg/20220531/f75951555b6f4d71931e2acee5a8a13d/13e103235a0a47299caff7500bdb48ef.png",
		"menuLinkType": "0",
		"menuTip": "按钮提示语"
	}]
}
'''



data = json.loads(json_str)

# 将JSON数据转换为去掉空格的形式
formatted_json = json.dumps(data, separators=(',', ':'))

# 打印结果
print(formatted_json.encode('utf-8').decode('unicode_escape'))