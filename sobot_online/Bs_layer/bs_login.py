# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.common.file_dealing import *
import requests, re, json
from urllib.parse import urlencode


class Login:
    def __init__(self):
        config_detail = load_yaml_file(filepath=r"/config_file/operation_config.yml")["config"]
        config_file = load_yaml_file(filepath=r"/config_file/service_data.yml")[f"{config_detail}"]
        loginPwd = config_file["PWD"]
        loginUser = config_file["EMAIL"]
        self.host = config_file["HOST"]
        try:
            self.host2 = config_file["HOST2"]
            print(f"\nself.host2的值为：{self.host2}\n")
        except Exception as e:
            print(f"e 的值为{e}")
        self.bno = config_file["SYSNUM"]
        self.sb = config_file["Sysbol"]
        self.session = requests.session()
        # 关闭多余的链接 用来解决  Max retries exceeded with url
        # 增加重试连接次数：
        requests.DEFAULT = 5
        # 关闭多余的链接：
        self.session.keep_alive = False
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
        else:
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
        try:
            response = self.session.post(url, headers=headers, data=data)
            # print(f"response >>>  ：{response.text}")
            item_value= json.loads(response.text).get("item")
            # print(f"self.tempid >>>  ：{self.tempid}")
            if len(item_value) > 100:
                self.tempid = item_value
            else:
                self.tempid = None
        except Exception as e:
            print(f"异常原因为 >>>  ：{e}")
            self.tempid = None