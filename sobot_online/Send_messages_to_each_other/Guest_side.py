# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：访客端
# 在linux 环境中运行，需要将项目 根目录 路径添加到python 的环境变量中
import os
import sys

# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print("root_path的值为：%s" % root_path)
# sys.path.append(root_path)

import json, re
import requests
from urllib.parse import urlencode
from sobot_online.common.file_dealing import *


class Customer:
    def __init__(self):
        config_detail = load_yaml_file(filepath=r"/config_file/operation_config.yml")["config"]
        config_file = load_yaml_file(filepath=r"/config_file/service_data.yml")[f"{config_detail}"]
        # print(f"config_file  类运行前运行了这个代码{config_file}")
        self.host = config_file["HOST"]
        self.bno = config_file["SYSNUM"]
        self.session = requests.session()

    # 1、获取用户信息配置
    def get_config(self):
        url = self.host + "/chat-visit/user/config.action"
        payload = {
            "sysNum": str(self.bno),
            "source": 0,
            "robotFlag": None,
            "channelFlag": None,
            "faqId": None, }
        headers = {
            'bno': str(self.bno),
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=payload)
        print(response.text)

    # 2、获取访客信息配置，获取cid，uid
    def customer_info_init(self, partnerid: str = "nnnd",uname="", source=0, channelFlag=None, face="",isVip="0"):
        """
        :param isVip:
        :param uname:
        :param partnerid:
        :param source: 0web，1移动，2APP，3微信
        :param channelFlag:
        :param face:
        :return:
        """
        url = self.host + "/chat-visit/user/init.action"
        data = urlencode(
            {
                "ack": "1",
                "sysNum": self.bno,
                "source": source,
                "chooseAdminId": "",
                "tranFlag": "0",
                "groupId": "",
                "partnerId": partnerid,
                "tel": "",
                "email": "",
                "uname": uname + "--猜猜我是谁",
                "visitTitle": "",
                "visitUrl": "",
                "face": face,
                "realname": uname + "--真实姓名",
                "weibo": "",
                "weixin": "",
                "qq": "",
                "sex": "",
                "birthday": "",
                "remark": "",
                "params": "",
                "isReComment": "1",
                "customerFields": "",
                "visitStartTime": "",
                "agid": "",
                "multiParams": "",
                "summaryParams": "",
                "channelFlag": channelFlag,
                "isVip": isVip,
                "vipLevel": "",
                "userLabel": "",
                "xst": "",
                "isJs": "0",
                "joinType": ""
            }
        )
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        rest = json.loads(response.text)
        print(f"rest 的值为：{rest}")
        uid = rest["uid"]
        cid = rest["cid"]
        pid = rest["pid"]
        print(f"uid>>>：{uid}, cid>>>：{cid}, pid>>>：{pid}source>>>：{source},channelFlag 的值为：{channelFlag}")
        return uid, cid,pid

    # 3.1、与机器人发送消息
    def send_message_to_robot(self, uid, cid, requestText, robotFlag="1"):
        url = self.host + "/chat-web/user/robotsend/v2.action"
        data = urlencode({
            "requestText": requestText,
            "question": requestText,
            "uid": str(uid),
            "cid": str(cid),
            "source": "0",
            "questionFlag": "0",
            "lanFlag": "1",
            "robotFlag": robotFlag,
            "adminId": "",
            "tranFlag": "0",
            "groupId": "",
            "transferAction": "",
            "flowType": "",
            "flowCompanyId": "",
            "flowGroupId": "",
            "sourceFrom": "",
            "ruleId": "",
            "inputType": "sendArea"
        })
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data, verify=False)
        print(response.text, sep="\n")

    # 3.2、转人工。通过初始化得到的uid，cid 与工作台建立链接，获取puid，并通过这三个参数与工作台进行会话
    def chat_connection(self, uid, cid, groupId=None):
        url = self.host + "/chat-web/user/chatconnect.action"
        data = {
            "sysNum": self.bno,
            "uid": uid,
            "cid": cid,
            "chooseAdminId": "",
            "tranFlag": "0",
            "current": "false",
            "groupId": groupId,
            "keyword": "",
            "keywordId": "",
            "queueFlag": "",
            "transferType": "0",
            "transferAction": "",
            "adminHelloWord": "",
            "activeTransfer": "1",
            "unknownQuestion": "",
            "docId": "",
            "answerMsgId": "",
            "ruleId": "",
            "flowType": "",
            "flowCompanyId": "",
            "flowGroupId": ""
        }
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        puid = json.loads(response.text).get("puid")
        status = json.loads(response.text).get("status")
        print(f"chat_connection   中的 response.text>>>：{response.text}")
        print(f"chat_connection   中的 puid>>>：{puid}")
        print(f"chat_connection   中的 status>>>：{status}")
        rest = json.loads(response.text)
        return rest

    # 4、 离线动作
    def out_action(self, uid):
        url = self.host + "/chat-web/user/out.action"
        data = {"uid": uid}
        headers = {
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)

    # 5、获取工作台发送的信息
    def receipt_msg(self):
        url = "https://hk.sobot.com/chat-msg/user/msg.action"
        data = {
            "first": "",
            "puid": "35b54f925ca94714b5353474159736ef",
            "uid": "9201b2fe6c2b410e913d37dd3ac712e4",
            "token": ""
        }
        headers = {
            'bno': '913d909e3a194598ba61cf904b5dc12a',
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)

    # 6、给工作台发送消息
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
            'bno': self.bno,
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = self.session.post(url, headers=headers, data=data)
        print(f"puid>>>：{puid}, uid>>>:{uid}, cid>>>:{cid}")
        print(f"访客端返回数据response.text>>>:{response.text}")

    # 7、发送留言
    def allot_leave_msg(self, uid, groupId=None, content=f"这是这个客户的第：{str(random.randint(1000, 9999))}条留言记录"):
        url = self.host + "/chat-web/user/allotLeaveMsg.action"
        data = {
            'uid': uid,
            'groupId': groupId,
            'content': content
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.session.post(url, headers=headers, data=data)
        rest = json.loads(response.text)
        print(f"发送留言  生效>>>：{rest}")
        return rest

    # 8.1、获取满意度评价模板数据
    def satisfaction_message_data(self, uid):
        url = self.host + "/chat-web/user/satisfactionMessage/v2.action"
        params = {
            "uid": uid
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        response = self.session.get(url=url, headers=headers, params=params)
        satisfaction_info = json.loads(response.text).get("data")
        return satisfaction_info

    #  8.2、进行满意度评价
    def comment(self, cid, uid,score=0, tag="",solved="0", remark=None, satisfy_type=0,commentType="1",scoreFlag=0, scoreExplain="",satisfaction_info=None):
        """
        :param cid:
        :param uid:
        :param score:
        :param tag:
        :param solved:
        :param remark:
        :param satisfy_type:
        :param commentType: 0:邀请评价，1：主动评价
        :param scoreFlag:
        :param scoreExplain:
        :param satisfaction_info:
        :return:
        """
        url = self.host + "/chat-web/user/comment.action"
        if satisfaction_info:
            if len(satisfaction_info) > 1:
                get_score_info = satisfaction_info[random.randint(0, len(satisfaction_info) - 1)]
            else:
                get_score_info = satisfaction_info[0]
            score = get_score_info["score"]
            scoreFlag = get_score_info["scoreFlag"]
            scoreExplain = get_score_info["scoreExplain"]
            satisfy_type =1
            if get_score_info["labelName"]:
                tag_list = get_score_info["labelName"].split(",")
                tag = tag_list[-1]
        data = {
            "cid": cid,
            "visitorId": uid,
            "score": score,
            "solved": solved,
            "tag": tag,
            "robotFlag": "",
            "remark": remark,
            "type": satisfy_type,
            "commentType": commentType,
            "scoreFlag": scoreFlag,
            "scoreExplain": scoreExplain
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        response = self.session.post(url=url, headers=headers, data=data)
        print(response.text)


if __name__ == '__main__':
    pass
    obj = Customer()
    # # uid, cid = obj.customer_info_init()
    # # rest = obj.chat_connection(uid=uid, cid=cid)
    # # puid = rest.get("puid")
    # # status = rest.get("status")
    # # print(f"puid >>>>：{puid}")
    # # print(f"status >>>>：{status}")
    # # obj.send_message_to_workbranch(puid, uid=uid, cid=cid)
    # obj.allot_leave_msg(uid="3cddfeb0e813a53aa8092b692bd8412e", groupId="e1536b360f61457789b1d3338f01c5ae")
    # config_detail = load_yaml_file(
    # obj.satisfaction_message_data(uid="7d3e78b4b34d46d7b8e1ef3c4b71b5a1")
    obj.customer_info_init(source=8, channelFlag="")