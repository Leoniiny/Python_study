# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import requests, re, json, base64
from urllib.parse import urlencode
class Graph():
    def __init__(self):
        self.session = requests.session()

    def submit_summary(self):
        url = "https://api-c.sobot.com/text/chat-kwb/conversation/summarySubmitVer2.action"
        data = {
                "updateServiceId": "blxFTKWZgBPImbc4ODpT4UN4X0yoq37qa0p6AjqcidvieqhpKlyK2jA5DTT2ZGM2",
                "uid": "a3211d7b33196ffba7d426d9e83bc5f1",
                "cid": "bebabf63a429459e8f035aed7e2b8c08",
                "pid": "cfd4681074ce4bed904928fb609fc824",
                "questionStatus": "1",
                "operationId": "1694760600258",
                "operationName": "大学",
                "reqTypeIdPath": "1694760600264",
                "reqTypeNamePath": "双一流",
                "questionDescribe": "",
                "fields": [{"fieldId":"10cc9cb51e764a99986c8fe46d3ca825","fieldName":"AAA","fieldValue":"1111"}]
            }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'bNo': 'cfd4681074ce4bed904928fb609fc824',
        }
        response = self.session.post(url=url, headers=headers, data=data)
        print(response.text)

if __name__ == '__main__':
    pass
    obj = Graph()
    obj.submit_summary()