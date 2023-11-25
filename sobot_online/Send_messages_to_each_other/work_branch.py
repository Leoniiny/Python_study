# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服工作台
import os
import sys

# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print("root_path的值为：%s" % root_path)
# sys.path.append(root_path)

import requests, re, json, base64
from urllib.parse import urlencode
from sobot_online.common.file_dealing import *



class WorkBranch:
    def __init__(self):
        config_detail = load_yaml_file(filepath=r"/config_file/operation_config.yml")["config"]
        config_file = load_yaml_file(filepath=r"/config_file/service_data.yml")[f"{config_detail}"]
        # print(f"config_file  类运行前运行了这个代码{config_file}")
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
    def get_tid(self, serviceId):
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
    def login_workbranche(self, tid, st="1"):
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

    # 邀请评价
    def recomment(self, tid, cid, uid):
        url = self.host + "/chat-kwb/admin/reComment.action"
        data = {
            "tid": tid,
            "cid": cid,
            "uid": uid
        }
        headers = {
            'bNo': self.bno,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url=url, headers=headers, data=data)
        print(response.text)

    # 提交服务总结《这里需要区分V1和V6》
    # A、获取服务总结列表
    def get_unit_infos(self, tid):
        url = self.host + "/chat-kwb/conversation/getUnitInfos.action"
        data = {
            "tid": tid
        }
        headers = {
            'bNo': self.bno,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url=url, headers=headers, data=data)
        unit_infos_list = json.loads(response.text).get("items")
        return unit_infos_list

    # B、获取服务总结某一个业务单元的内容
    def get_unifo_body(self, tid, cid):
        url = self.host + "/chat-kwb/conversation/getUnifoInfoById.action"
        unit_infos_list = self.get_unit_infos(tid=tid)
        if unit_infos_list:
            random_num = random.randint(0, len(unit_infos_list) - 1)
            unit_info = unit_infos_list[random_num]
            unitId = unit_info["unitId"]
            data = {
                "tid": tid,
                "cid": cid,
                "unitId": unitId
            }
            headers = {
                'bNo': self.bno,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = self.session.post(url=url, headers=headers, data=data)
            try:
                unit_body_list = json.loads(response.text).get("item").get("typeList")
                unit_fieldList = json.loads(response.text).get("item").get("fieldList")
                return unit_info,unit_body_list, unit_fieldList
            except Exception as e:
                print(f"这个服务总结没有业务分类：{e}")

    # C、提交服务总结
    def submmit_summary(self, tid, uid, cid, pid, questionStatus=0, reqTypeIdPath="", reqTypeNamePath="",questionDescribe="",
                        fields="", fields_value="", unit_info=None, unit_body_list=None, unit_fieldList=None):
        """
        :param fields_value:
        :param tid:
        :param uid:
        :param cid:
        :param pid:
        :param questionStatus:
        :param reqTypeIdPath:
        :param reqTypeNamePath:
        :param questionDescribe:
        :param fields:
        :param unit_info: 业务单元内容
        :param unit_body_list: 业务分类列表
        :param unit_fieldList: 业务分类的自定义字段
        :return:
        """
        url = self.host + "/chat-kwb/conversation/summarySubmitVer2.action"
        headers = {
            'bNo': self.bno,
            'Content-Type': "application/x-www-form-urlencoded"
        }
        # 有效记录
        if unit_info:
            operationId = unit_info.get("unitId")
            operationName = unit_info.get("unitName")
            if unit_body_list:
                if len(unit_body_list) > 1:
                    reqTypeIdPath = unit_body_list[random.randint(0, len(unit_body_list) - 1)].get("typeId")
                    reqTypeNamePath = unit_body_list[random.randint(0, len(unit_body_list) - 1)].get("typeName")
                else:
                    reqTypeIdPath = unit_body_list[0].get("typeId")
                    reqTypeNamePath = unit_body_list[0].get("typeName")
            if unit_fieldList:
                fields = []
                if len(unit_fieldList) > 1:
                    new_field_dic = {
                        "fieldId": unit_fieldList[random.randint(0, len(unit_fieldList) - 1)].get("fieldId"),
                        "fieldName": unit_fieldList[random.randint(0, len(unit_fieldList) - 1)].get("fieldName"),
                        "fieldValue": fields_value
                    }
                else:
                    new_field_dic = {
                        "fieldId": unit_fieldList[0].get("fieldId"),
                        "fieldName": unit_fieldList[0].get("fieldName"),
                        "fieldValue": fields_value
                    }
                fields.append(new_field_dic)
            data = urlencode(
                {
                    "updateServiceId": tid,
                    "uid": uid,
                    "cid": cid,
                    "pid": pid,
                    "questionStatus": questionStatus,
                    "operationId": operationId,
                    "operationName": operationName,
                    "reqTypeIdPath": reqTypeIdPath,
                    "reqTypeNamePath": reqTypeNamePath,
                    "questionDescribe": questionDescribe,
                    "fields": fields
                }
            )
        # 无效会话
        else:
            data = urlencode(
                {
                    "updateServiceId": tid,
                    "uid": uid,
                    "cid": cid,
                    "invalidSession": 1
                }
            )
        response = self.session.post(url=url, headers=headers, data=data)
        print(f"\n\n\n提交满意度评价的结果为  >>>：{json.loads(response.text)}\n\n\n\n")


if __name__ == '__main__':
    pass
    obj = WorkBranch()
    # serviceId = obj.service_menus()
    # tid = obj.get_tid(serviceId=serviceId)
    # obj.login_workbranche(tid=tid)
    # obj.send_msg_to_customer(tid=tid, uid="", cid="")
    # rest = obj.get_unit_infos(tid=tid)
    # print(rest)
