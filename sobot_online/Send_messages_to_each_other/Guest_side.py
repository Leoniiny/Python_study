# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：访客端
import json, re
import requests
from urllib.parse import urlencode


class Customer:
    def __init__(self):
        self.session = requests.session()

    # 1、获取用户信息配置
    def get_config(self):
        url = "https://hk.sobot.com/chat-visit/user/config.action"
        payload = {
            "sysNum": "913d909e3a194598ba61cf904b5dc12a",
            "source": 0,
            "robotFlag": None,
            "channelFlag": None,
            "faqId": None, }
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    # 2、获取访客信息配置，获取cid，uid
    def customer_info_init(self, partnerid: str = "qnmd"):
        url = "https://hk.sobot.com/chat-visit/user/init.action"
        data = {
            "ack": "1",
            "sysNum": "913d909e3a194598ba61cf904b5dc12a",
            "source": "0",
            "chooseAdminId": "",
            "tranFlag": "0",
            "groupId": "",
            "partnerId": partnerid,
            "tel": "",
            "email": "",
            "uname": partnerid + "猜猜我是谁",
            "visitTitle": "",
            "visitUrl": "",
            "face": "",
            "realname": "",
            "weibo": "",
            "weixin": "",
            "qq": "",
            "sex": "",
            "birthday": "",
            "remark": "",
            "params": "",
            "isReComment": "1",
            "customerFields": "",
            "visitStartTime": "",
            "agid": "",
            "multiParams": "",
            "summaryParams": "",
            "channelFlag": "",
            "isVip": "",
            "vipLevel": "",
            "userLabel": "",
            "xst": "",
            "isJs": "0",
            "joinType": ""
        }

        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post( url, headers=headers, data=data)
        rest = json.loads(response.text)
        uid = rest["uid"]
        cid = rest["cid"]
        print(response.text, uid, cid, sep='\n')
        return uid, cid

    # 3.1、与机器人发送消息
    def send_message_to_robot(self,uid,cid):
        url = "https://hk.sobot.com/chat-web/user/robotsend/v2.action"
        data = urlencode({
            "requestText": "纯文本",
            "question": "纯文本",
            "uid": str(uid),
            "cid": str(cid),
            "source": "0",
            "questionFlag": "0",
            "lanFlag": "1",
            "robotFlag": "1",
            "adminId": "",
            "tranFlag": "0",
            "groupId": "",
            "transferAction": "",
            "flowType": "",
            "flowCompanyId": "",
            "flowGroupId": "",
            "sourceFrom": "",
            "ruleId": "",
            "inputType": "sendArea"
        })
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text, sep="\n")

    # 3.2、通过初始化得到的uid，cid 与工作台建立链接，获取puid，并通过这三个参数与工作台进行会话
    def chat_connection(self,uid, cid):
        url = "http://hk.sobot.com/chat-web/user/chatconnect.action"
        data = {
            "sysNum": "913d909e3a194598ba61cf904b5dc12a",
            "uid": str(uid),
            "cid": str(cid),
            "chooseAdminId": "",
            "tranFlag": "0",
            "current": "false",
            "groupId": "",
            "keyword": "",
            "keywordId": "",
            "queueFlag": "",
            "transferType": "0",
            "transferAction": "",
            "adminHelloWord": "",
            "activeTransfer": "1",
            "unknownQuestion": "",
            "docId": "",
            "answerMsgId": "",
            "ruleId": "",
            "flowType": "",
            "flowCompanyId": "",
            "flowGroupId": ""
        }
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        # print(response.text)
        puid = json.loads(response.text).get("puid")
        print(puid, cid, uid, sep="\n")
        return puid

    # 4、 离线动作
    def out_action(self):
        url = "http://hk.sobot.com/chat-web/user/out.action"
        data = {"uid": "e26b9ec6eeaf1d491470315b98e55810"}
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)

    # 5、获取工作台发送的信息
    def receipt_msg(self):
        url = "https://hk.sobot.com/chat-msg/user/msg.action"
        data = {
            "first": "",
            "puid": "35b54f925ca94714b5353474159736ef",
            "uid": "9201b2fe6c2b410e913d37dd3ac712e4",
            "token": ""
        }
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)


if __name__ == '__main__':
    pass
    # obj01 = get_config()
    obj02 = Customer().customer_info_init()
    # obj03 = Customer().msg()
    # obj03 = Customer().send_message()
    # obj03 = Customer().chat_connection()
    # print(Customer().uid)
