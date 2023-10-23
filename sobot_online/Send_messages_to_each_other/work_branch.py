# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服工作台
import requests, re, json, base64
from sobot_online.common.file_dealing import *

config_detail= load_yaml_file(filepath=r"\config_file\operation_config.yml")["config"]
config_file = load_yaml_file(filepath=r"\config_file\service_data.yml")[f"{config_detail}"]
print(f"config_file  类运行前运行了这个代码{config_file}")


class WorkBranch:
    def __init__(self):
        config_detail = load_yaml_file(filepath=r"\config_file\operation_config.yml")["config"]
        config_file = load_yaml_file(filepath=r"\config_file\service_data.yml")[f"{config_detail}"]
        print(f"config_file  类运行前运行了这个代码{config_file}")
        loginPwd = config_file["PWD"]
        loginUser = config_file["EMAIL"]
        self.host = config_file["HOST"]
        self.bno = config_file["SYSNUM"]
        self.sb = config_file["Sysbol"]
        self.session = requests.session()
        if self.sb == "HK":
            url = self.host + "/basic-login/serviceLogin/4"
            data = {
                "loginUser": loginUser,
                "loginPwd": loginPwd,
                "randomKey": "",
                "loginFlag": "1",
                "terminalCode": ""
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        if self.sb == "TX" or "AL":
            url = self.host + "/basic-login/account/consoleLogin/4"
            data = json.dumps({
                "loginUser": loginUser,
                "loginPwd": str(loginPwd),
                "randomKey": "",
                "loginFlag": "1",
                "terminalCode": ""
            })
            headers = {
                'Content-Type': 'application/json',
            }
        response = self.session.post(url, headers=headers, data=data)
        self.tempid = json.loads(response.text).get("item")
        # print(f"self.tempid >>>  ：{self.tempid}")
        # print(f"loginPwd >>>  ：{loginPwd}")
        # print(f"loginUser >>>  ：{loginUser}")
        # print(f"self.host >>>  ：{self.host}")

    # 获取客服信息配置
    def service_menus(self):
        url = self.host + "/basic-config-service/consoleAuth/queryAgentMenus?language=zh"
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.get(url, headers=headers)
        serviceId = json.loads(response.text).get("item").get("serviceId")
        # print(f"serviceId  的值：{serviceId}")
        return serviceId

    # 获取工作台tid
    def get_tid(self,serviceId):
        # serviceId = self.service_menus()
        url = self.host + "/chat-web/webchat/toChat.action"
        params = {
            "uid": str(serviceId),
            "status": "1",
            "version": "2",
            "token": str(self.tempid)
        }
        response = self.session.get(url, params=params, allow_redirects=False)
        tid = re.findall("id=(.*?)&lt", json.dumps(str(response.headers)))[0]
        print(f"tid 的值为：{tid}")
        return str(tid)

    # 登录客服工作台
    def login_workbranche(self,tid,st="1"):
        url = self.host + "/chat-kwb/admin/aci.action"
        data = {
            "uid": tid,
            "way": "1",
            "st": st,
            "lt": "",
            "token": self.tempid,
            "ack": "1",
            "isNew": "1"
        }
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url=url, headers=headers, data=data)
        print(response.text)

    # 发送消息到访客端
    def send_msg_to_customer(self, tid,uid, cid, content=str("工作台：随便发送点啥都行")):
        # tid = "UXpRM2TWy+f1F38hfGISwqBtjjX8YdfyDu/QQAPpy+UYW1u4KZXp90sdBegyJt+T"
        url = self.host + "/chat-kwb/message/send.action"
        payload = {
            "tid": tid,
            "cid": cid,
            "uid": uid,
            "msgType": "0",
            "content": content,
            "objMsgType": "",
            "docId": "",
            "replyId": "",
            "fileName": "",
            "msgId": "",
            "title": "",
            "answerId": "'"
        }
        headers = {
            'bno': str(self.bno),
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url, headers=headers, data=payload)
        print(f"工作台返回数据response.text>>>:{response.text}")

    # 调用离线接口
    def service_out(self, uid):
        url = self.host + "/chat-kwb/admin/out.action"
        data = {
            "uid": uid
        }
        headers = {
            "Content - Type": "application / x - www - form - urlencoded"
        }
        response = self.session.post(url, headers=headers, data=data)
        print(f"response 的值为：{response.text}")


if __name__ == '__main__':
    pass
    obj = WorkBranch()
    serviceId = obj.service_menus()
    tid= obj.get_tid(serviceId=serviceId)
    obj.login_workbranche(tid=tid)
    obj.send_msg_to_customer(tid=tid,uid="",cid="")
