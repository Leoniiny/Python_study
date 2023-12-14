# @Time : 2023/11/25 23:06
# @Author : 雷洋平
# @File : console_setting.py
# @Software: PyCharm
# @Function:控制台 设置
from sobot_online.common.file_dealing import *
import requests, re, json


class ConsoleSetting:
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
        response = self.session.post(url, headers=headers, data=data)
        self.tempid = json.loads(response.text).get("item")
        print(f"self.tempid >>>  ：{self.tempid}")

    # 上传图片
    def uploading_images(self, file_content=None):
        url = self.host + "/chat-web/webchat/expressionUpload"
        data = {
            "pid": self.bno,
        }
        files = {
            "file": file_content
        }
        headers = {
            "Temp-Id": self.tempid
        }
        response = self.session.post(url=url, headers=headers, data=data, files=files)
        img_url = ""
        try:
            img_url = json.loads(response.text).get("item").get("url")
            return img_url
        except Exception as e:
            print(f"\n response 的结果为：{json.loads(response.text)}；\n\ne 的返回值为：{e}；\n")
            return img_url

    # 获取PC\h5 的所有子渠道
    def get_child_source(self, channelType=1):
        """
        :param channelType: 0web，1移动，2APP，3微信
        :return:
        """
        url = self.host + "/chat-set/rest/selectConfigInfo/4"
        params = {
            "channelType": channelType,
            "current":1,
            "pageSize":100
        }
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.get(url=url, headers=headers, params=params)
        print(f"\n response 的值为》》》：{response.text}\n\n")
        try:
            channelFlag_list = [child_source_info.get("channelFlag") for child_source_info in json.loads(response.text)["list"]]
            print(f"\nchannelFlag_list 的值为》》》：{channelFlag_list}\n\n")
            return channelFlag_list
        except Exception as e:
            channelFlag_list= []
            print(f"\ne 的值为{e}\n")
            print(f'\njson.loads(response.text)["list"] 的值为》》》：{json.loads(response.text)["list"]}\n')
            return channelFlag_list


if __name__ == '__main__':
    pass
    # img_num = random.randint(1,31)
    # print(f"img_num 的值为：{img_num}")
    # file_content = (f"p{img_num}.jpg", open(DATA_PATH + fr"\imgs\p{img_num}.jpg", mode="rb"),'image/jpg')
    obj = ConsoleSetting()
    # obj.uploading_images(file_content=file_content)
    obj.get_child_source(channelType=1)
