# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import threading
import time, re, json, requests
from urllib.parse import urlencode


class Multi_Thread:
    def __init__(self, host='https://test.sobot.com'):
        self.session = requests.session()
        self.host = host

    def out_action(self, uid):
        '''
        用户离线
        :param uid:
        :return:
        '''
        url = self.host + "/chat-web/user/out.action"
        data = {"uid": uid}
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)

    def send_msg_to_customer(self, tid, uid, cid, content=str("工作台：随便发送点啥都行")):
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
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url, headers=headers, data=payload)
        print(f"工作台返回数据response.text>>>:{response.text}")

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
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(f"puid>>>：{puid}, uid>>>:{uid}, cid>>>:{cid}")
        print(f"访客端返回数据response.text>>>:{response.text}")


if __name__ == '__main__':
    host = 'https://api-c-grey.sobot.com/text'
    tid = 'OumStS1Q9ewDRdx73IY3WutAI8u3dc8Df19PIuYDz4QpLPz6gBq8dpWFOBidxAyN'
    uid = '30dc607f625d2ca0524399082aefcc24'
    puid = 'abd7b9a4984a4c538cef34eddebaf20b'
    cid = input('请输入 cid ：')
    t1 = threading.Thread(target=Multi_Thread(host=host).out_action, args=(uid,))
    t2 = threading.Thread(target=Multi_Thread(host=host).send_msg_to_customer, args=(tid, uid, cid))
    t3 = threading.Thread(target=Multi_Thread(host=host).send_message_to_workbranch, args=(puid, cid, uid))
    # test1：访客离线，工作台发送消息
    t1.start()
    t2.start()
    # test2：访客离线，访客端发送消息
    # t1.start()
    # t3.start()
