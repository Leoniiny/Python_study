# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服工作台
import requests, re, json, base64
from urllib.parse import urlencode
from sobot_online.common.file_dealing import *

class WorkBranch:
    def __init__(self):
        self.session = requests.session()
        url = "http://hk.sobot.com/basic-login/serviceLogin/4"
        data = urlencode({
            "loginUser": "lyp@hk.com",
            "loginPwd": "SGsxMjM0NTY=",
            "randomKey": "",
            "loginFlag": "1",
            "terminalCode": ""
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url, headers=headers, data=data)
        self.tempid = json.loads(response.text).get("item")

    # 客服登录
    def service_login(self):
        url = "http://hk.sobot.com/basic-login/serviceLogin/4"
        data = urlencode({
            "loginUser": "lyp@hk.com",
            "loginPwd": "SGsxMjM0NTY=",
            "randomKey": "",
            "loginFlag": "1",
            "terminalCode": ""
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url, headers=headers, data=data)
        self.tempid = json.loads(response.text).get("item")
        return self.tempid

    # 获取客服信息配置
    def service_menus(self):
        url = "http://hk.sobot.com/basic-config-service/consoleAuth/queryAgentMenus?language=zh"
        payload = {}
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'temp-id': self.tempid
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        serviceId = json.loads(response.text).get("item").get("serviceId")
        print(f"serviceId  的值：{serviceId}")
        return serviceId

    # 获取工作台tid
    def get_tid(self):
        url = "https://hk.sobot.com/chat-web/webchat/toChat.action"
        serviceId = self.service_menus()
        params = {
            "uid": str(serviceId),
            "status": "1",
            "version": "2",
            "token": str(self.tempid)
        }
        response = self.session.get(url, params=params, allow_redirects=False)
        tid = re.findall("id=(.*?)&lt", json.dumps(str(response.headers)))[0]
        print(tid)
        return str(tid)

    # 发送消息到访客端
    def send_msg_to_customer(self,uid,cid):
        url = "https://hk.sobot.com/chat-kwb/message/send.action"
        tid = self.get_tid()
        payload = {
            "tid": tid,
            "cid": cid,
            "uid": uid,
            "msgType": "0",
            "content": "情话",
            "objMsgType": "",
            "docId": "",
            "replyId": "",
            "fileName": "",
            "msgId": "",
            "title": "",
            "answerId": "'"
        }
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url, headers=headers, data=payload)
        print(response.text)
        print("self.tid >>>:",tid)


if __name__ == '__main__':
    pass
    # obj = WorkBranch().service_login()
    obj = WorkBranch().service_menus()
    # obj = WorkBranch().get_tid()


