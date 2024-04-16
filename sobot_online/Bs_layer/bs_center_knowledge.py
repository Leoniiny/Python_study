# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from faker import Faker
from sobot_online.Bs_layer.bs_login import Login
import requests
fk = Faker(locale="zh_CN")

class KB_center(Login):
    def __init__(self):
        super().__init__()
        self.FK = Faker(locale="zh_CN")

    def add_content(self, kbId="1", kbType="1", questionTitle=fk.word(),questionTypeId="e23426ce3b2644838043580def58ac32"):
        url = self.host + "/kb-inner-service/innerDoc/save"
        json_data = {
            "answerDesc": f"{self.FK.text() + self.FK.text() + self.FK.text() + self.FK.text() + self.FK.text() + self.FK.text()}",
            "answerTxt": "",
            "cover": "",
            "effectStatus": 1,
            "effectTime": "2024-04-07 00:00",
            "invalidTime": "2024-04-07 23:59",
            "kbId": kbId,
            "kbType": kbType,
            "questionTitle": questionTitle,
            "questionTypeId": questionTypeId
        }
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid,
            'timezone': '+08:00',
            'timezoneid': 'Asia/Shanghai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        kb_add_resp = self.session.post(url, headers=headers, json=json_data)
        print(kb_add_resp.text)

    def add_type(self,questionTypeName,kbId="1",parentTypeId="-1"):
        url = self.host + "/kb-inner-service/questionType/add"
        json_data = {
            "kbId": kbId,
            "questionTypeName": questionTypeName,
            "parentTypeId": parentTypeId
        }
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid,
            'timezone': '+08:00',
            'timezoneid': 'Asia/Shanghai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        kb_add_type = self.session.post(url,headers=headers,json=json_data)
        print(kb_add_type.text)


if __name__ == '__main__':
    obj = KB_center()
    for i in range(500):
        obj.add_content(questionTitle =fk.word()+str(i) ,questionTypeId="d48b7708d82a4e44bf8fa317b4d80ab4")

