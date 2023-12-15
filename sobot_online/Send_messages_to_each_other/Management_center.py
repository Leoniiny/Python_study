# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：管理中心
import requests, re, json, base64,random
from sobot_online.Send_messages_to_each_other.console_setting import ConsoleSetting
from urllib.parse import urlencode


class MangeCenter(ConsoleSetting):
    def __init__(self):
        super().__init__()

    def get_satis_templates(self):
        url = self.host + "/chat-satisfaction/saticfaction/getTemplateList"
        headers = {
            'bNo': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.get(url, headers=headers)
        if response.text:
            try:
                score_ten = [template.get('id') for template in json.loads(response.text).get("items") if template.get('scoreFlag') == 0]
                score_five = [template.get('id') for template in json.loads(response.text).get("items") if template.get('scoreFlag') == 1]
                print(f"\nscore_ten >>>：{score_ten},score_five >>>：{score_five}\n")
                return score_ten,score_five
            except Exception as e:
                print(e)


if __name__ == '__main__':
    pass
    obj = MangeCenter()
    li_1,li_2 = obj.get_satis_templates()