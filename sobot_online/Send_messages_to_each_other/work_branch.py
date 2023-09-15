# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服工作台
import requests, re, json, base64
from urllib.parse import urlencode
from sobot_online.common.file_dealing import *
hk_config = load_yaml_file(filepath=r"\config_file\service_data.yml")["HK"]


class WorkBranch:
    def __init__(self):
        loginPwd = hk_config["PWD"]
        loginUser = hk_config["EMAIL"]
        self.host = hk_config["HOST"]
        self.bno = hk_config["SYSNUM"]
        self.session = requests.session()
        url = self.host + "/basic-login/serviceLogin/4"
        data = urlencode({
            "loginUser": loginUser,
            "loginPwd": loginPwd,
            "randomKey": "",
            "loginFlag": "1",
            "terminalCode": ""
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url, headers=headers, data=data)
        self.tempid = json.loads(response.text).get("item")

    # 获取客服信息配置
    def service_menus(self):
        url = self.host + "/basic-config-service/consoleAuth/queryAgentMenus?language=zh"
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.get(url, headers=headers)
        serviceId = json.loads(response.text).get("item").get("serviceId")
        print(f"serviceId  的值：{serviceId}")
        return serviceId

    # 获取工作台tid
    def get_tid(self,serviceId):
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

    # 发送消息到访客端
    def send_msg_to_customer(self,tid,uid,cid,content=str("工作台：随便发送点啥都行")):
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
    def service_out(self,uid):
        url = self.host + "/chat-kwb/admin/out.action"
        data = {
            "uid":uid
        }
        headers = {
            "Content - Type": "application / x - www - form - urlencoded"
        }
        response = self.session.post(url, headers=headers, data=data)
        print(f"response 的值为：{response.text}")


if __name__ == '__main__':
    pass
    serviceId = WorkBranch().service_menus()
    tid= WorkBranch().get_tid(serviceId=serviceId)
    WorkBranch().send_msg_to_customer(tid,uid="0de6619dcfdf451b934ca4ce754b7763",cid="8a8e772d7a754ff8a0cf1d9bc857c10c")
    WorkBranch().service_out(tid)



