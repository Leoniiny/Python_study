# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：管理中心
import json
from sobot_online.Bs_layer.bs_login import *


class MangeCenter(Login):
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
                score_ten = [template.get('id') for template in json.loads(response.text).get("items") if
                             template.get('scoreFlag') == 0]
                score_five = [template.get('id') for template in json.loads(response.text).get("items") if
                              template.get('scoreFlag') == 1]
                print(f"\nscore_ten >>>：{score_ten}\nscore_five >>>：{score_five}\n")
                return score_ten, score_five
            except Exception as e:
                print(e)

    def save_seg_ruler(self,ruleTitle='"无效数据1"',isEnabled=0):
        url = self.host + "/rule-service/rule/save"
        json_data = {
            "ruleTitle": ruleTitle,
            "isEnabled": isEnabled,
            "ruleScopeList": [1],
            "ruleGroupList": [{
                "ruleDetailList": [{
                    "ruleType": 2,
                    "ruleOptType": 0,
                    "ruleRel": 0,
                    "zoneString": "Asia/Shanghai",
                    "fieldList": [{
                        "fieldName": "time",
                        "fieldValue": "2024-05-02 10:02"
                    }]
                }]
            }]
        }
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid
        }

        response = requests.request("POST", url, headers=headers, json=json_data)

        print(response.text)


if __name__ == '__main__':
    pass
    obj = MangeCenter()
    for i in range(2,101):
        ruleTitle = "无效数据"+str(i)
        obj.segment(ruleTitle=ruleTitle)
