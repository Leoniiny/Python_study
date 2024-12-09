# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：多用户进线
import requests
from urllib.parse import urlencode
from faker import Faker
from sobot_online.common.file_dealing import *
fk = Faker(locale='zh_CN')
class MultiUserChat():
    def __init__(self,filepath = r"/config_file/customer_env.yml",env="AL"):
        super().__init__()
        customer_detail = load_yaml_file(filepath=filepath)[f"{env}"]
        self.host = customer_detail.get('host')
        self.sysNum = customer_detail.get('sysNum')
        self.groupId = customer_detail.get('groupId')
        self.env = env
        self.session = requests.session()
        self.time = get_current_timestamp(digits=10)

    def user_enter(self,chat_num =1,worker_id = None):
        url = self.host + "/chat-visit/user/init.action"
        name_id = str(random.randint(10000, 99999))
        partnerId = f"{self.env}-{name_id}"
        uname = f"Nickname:{self.env}-{name_id}"
        payload = f'sysNum={self.sysNum}&source=0&groupId={self.groupId}&uname={uname}&partnerId={partnerId}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}
        init_rest =self.session.post( url, headers=headers, data=payload).json()
        print(f"访客进线，init_rest:{init_rest}")
        uid = init_rest["uid"]
        cid = init_rest["cid"]
        url = self.host + "/chat-web/user/chatconnect.action"
        user_data ={
            "sysNum": f"{self.sysNum}",
            "uid": f"{uid}",
            "cid": f"{cid}",
            "chooseAdminId": "",
            "tranFlag": "0",
            "current": "false",
            "groupId": f"{self.groupId}"
}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}
        chatconnect_rest = self.session.post(url, headers=headers, data=user_data).json()
        puid = chatconnect_rest["puid"]
        print(f"访客进线，chatconnect_rest:{chatconnect_rest},\npuid:{puid},cid:{cid},uid:{uid}")

        for i in range(0, chat_num):
            time.sleep(0.5)     # 发送消息延时
            content = f"访客进线，消息：{i+1}"
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
                'bno': self.sysNum,
                'content-type': 'application/x-www-form-urlencoded',
            }
            user_send = self.session.post(url=url, headers=headers, data=data).json()
            print(f"这是第{i}次，访客端返回数据 user_send >>>：{user_send}")


            # if worker_id is not None:
            #     url =self.host +  "/chat-kwb/message/send.action"
            #     worker_context = fk.text(max_nb_chars=150).encode("utf-8")
            #     msgId = uid + str(self.time)
            #     data = {
            #         "tid": worker_id,
            #         "cid": cid,
            #         "uid": uid,
            #         "msgType": "0",
            #         "content": worker_context,
            #         "objMsgType": "",
            #         "docId": "",
            #         "replyId": "",
            #         "fileName": "",
            #         "msgId": msgId,
            #         "title": "",
            #         "answerId": "",
            #         "resend": ""
            #     }
            #     headers = {'content-type': 'application/x-www-form-urlencoded'}
            #     worker_send = self.session.post(url = url, headers=headers, data=data).json()
            #     print(f"客服端返回数据worker_send>>>：{worker_send}")



if __name__ == '__main__':
    multi_user = MultiUserChat(
        env="HKQ"
    )
    for i in range(1,301):
        multi_user.user_enter(

                              )
