# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：访客端
import json, re
import random

import requests
from urllib.parse import urlencode
from sobot_online.common.file_dealing import *


class Customer:
    def __init__(self):
        config_detail = load_yaml_file(filepath=r"\config_file\operation_config.yml")["config"]
        config_file = load_yaml_file(filepath=r"\config_file\service_data.yml")[f"{config_detail}"]
        print(f"config_file  类运行前运行了这个代码{config_file}")
        self.host = config_file["HOST"]
        self.bno = config_file["SYSNUM"]
        self.session = requests.session()

    # 1、获取用户信息配置
    def get_config(self):
        url = self.host + "/chat-visit/user/config.action"
        payload = {
            "sysNum": str(self.bno),
            "source": 0,
            "robotFlag": None,
            "channelFlag": None,
            "faqId": None, }
        headers = {
            'bno': str(self.bno),
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    # 2、获取访客信息配置，获取cid，uid
    def customer_info_init(self, partnerid: str = "nnnd", channelFlag=None,face=""):
        url = self.host + "/chat-visit/user/init.action"
        # print(f"url >>> ： {url}")
        data = {
            "ack": "1",
            "sysNum": self.bno,
            "source": "0",
            "chooseAdminId": "",
            "tranFlag": "0",
            "groupId": "",
            "partnerId": partnerid,
            "tel": "",
            "email": "",
            "uname": partnerid + "--猜猜我是谁",
            "visitTitle": "",
            "visitUrl": "",
            "face": face,
            "realname": partnerid + "--真实姓名",
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
            "channelFlag": channelFlag,
            "isVip": "",
            "vipLevel": "",
            "userLabel": "",
            "xst": "",
            "isJs": "0",
            "joinType": ""
        }
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        rest = json.loads(response.text)
        uid = rest["uid"]
        cid = rest["cid"]
        print(f"uid>>>：{uid}, cid>>>：{cid}")
        return uid, cid

    # 3.1、与机器人发送消息
    def send_message_to_robot(self, uid, cid, requestText,robotFlag="1"):
        url = self.host + "/chat-web/user/robotsend/v2.action"
        data = urlencode({
            "requestText": requestText,
            "question": requestText,
            "uid": str(uid),
            "cid": str(cid),
            "source": "0",
            "questionFlag": "0",
            "lanFlag": "1",
            "robotFlag": robotFlag,
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
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data, verify=False)
        print(response.text, sep="\n")

    # 3.2、转人工。通过初始化得到的uid，cid 与工作台建立链接，获取puid，并通过这三个参数与工作台进行会话
    def chat_connection(self, uid, cid, groupId=None):
        url = self.host + "/chat-web/user/chatconnect.action"
        data = {
            "sysNum": self.bno,
            "uid": uid,
            "cid": cid,
            "chooseAdminId": "",
            "tranFlag": "0",
            "current": "false",
            "groupId": groupId,
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
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        puid = json.loads(response.text).get("puid")
        status = json.loads(response.text).get("status")
        print(f"chat_connection   中的 response.text>>>：{response.text}")
        print(f"chat_connection   中的 puid>>>：{puid}")
        print(f"chat_connection   中的 status>>>：{status}")
        rest = json.loads(response.text)
        return rest

    # 4、 离线动作
    def out_action(self, uid):
        url = self.host + "/chat-web/user/out.action"
        data = {"uid": uid}
        headers = {
            'bno': self.bno,
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

    # 6、给工作台发送消息
    def send_message_to_workbranch(self, puid, cid, uid, content=str("访客端：随便发送点啥都行")):
        url = self.host + "/chat-web/message/user/send.action"
        data = urlencode({
            "puid": str(puid),
            "cid": str(cid),
            "uid": str(uid),
            "content": content,
            "objMsgType": "",
            "msgType": "0",
            "fileName": "undefined"
        })
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(f"puid>>>：{puid}, uid>>>:{uid}, cid>>>:{cid}")
        print(f"访客端返回数据response.text>>>:{response.text}")

    # 7、发送留言
    def allot_leave_msg(self, uid, groupId=None, content=f"这是这个客户的第：{str(random.randint(1000, 9999))}条留言记录"):
        url = self.host + "/chat-web/user/allotLeaveMsg.action"
        data = {
            'uid': uid,
            'groupId': groupId,
            'content': content}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.session.post(url, headers=headers, data=data)
        rest = json.loads(response.text)
        print(rest)
        return rest


if __name__ == '__main__':
    pass
    # obj = Customer()
    # # uid, cid = obj.customer_info_init()
    # # rest = obj.chat_connection(uid=uid, cid=cid)
    # # puid = rest.get("puid")
    # # status = rest.get("status")
    # # print(f"puid >>>>：{puid}")
    # # print(f"status >>>>：{status}")
    # # obj.send_message_to_workbranch(puid, uid=uid, cid=cid)
    # obj.allot_leave_msg(uid="3cddfeb0e813a53aa8092b692bd8412e", groupId="e1536b360f61457789b1d3338f01c5ae")
    config_detail = load_yaml_file(filepath=r"\config_file\operation_config.yml")["config"]
    print(config_detail)
