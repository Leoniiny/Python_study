# @Time : 2023/11/25 23:06
# @Author : 雷洋平
# @File : bs_OnlineAgent.py
# @Software: PyCharm
# @Function:控制台 设置
from sobot_online.common.file_dealing import *
import requests, re, json
from urllib.parse import urlencode
from sobot_online.Bs_layer.bs_login import Login


class ConsoleSetting(Login):
    def __init__(self):
        super().__init__()
        # config_detail = load_yaml_file(filepath=r"/config_file/operation_config.yml")["config"]
        # config_file = load_yaml_file(filepath=r"/config_file/service_data.yml")[f"{config_detail}"]
        # loginPwd = config_file["PWD"]
        # loginUser = config_file["EMAIL"]
        # self.host = config_file["HOST"]
        # try:
        #     self.host2 = config_file["HOST2"]
        #     print(f"\nself.host2的值为：{self.host2}\n")
        # except Exception as e:
        #     print(f"e 的值为{e}")
        # self.bno = config_file["SYSNUM"]
        # self.sb = config_file["Sysbol"]
        # self.session = requests.session()
        # # 关闭多余的链接 用来解决  Max retries exceeded with url
        # # 增加重试连接次数：
        # requests.DEFAULT = 5
        # # 关闭多余的链接：
        # self.session.keep_alive = False
        # if self.sb == "HK":
        #     url = self.host + "/basic-login/serviceLogin/4"
        #     data = {
        #         "loginUser": loginUser,
        #         "loginPwd": loginPwd,
        #         "randomKey": "",
        #         "loginFlag": "1",
        #         "terminalCode": ""
        #     }
        #     headers = {
        #         'Content-Type': 'application/x-www-form-urlencoded',
        #     }
        # else:
        #     url = self.host + "/basic-login/account/consoleLogin/4"
        #     data = json.dumps({
        #         "loginUser": loginUser,
        #         "loginPwd": str(loginPwd),
        #         "randomKey": "",
        #         "loginFlag": "1",
        #         "terminalCode": ""
        #     })
        #     headers = {
        #         'Content-Type': 'application/json',
        #     }
        # try:
        #     response = self.session.post(url, headers=headers, data=data)
        #     # print(f"response >>>  ：{response.text}")
        #     self.tempid = json.loads(response.text).get("item")
        #     # print(f"self.tempid >>>  ：{self.tempid}")
        # except Exception as e:
        #     print(f"异常原因为 >>>  ：{e}")
        #     self.tempid = None

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
        :param channelType: 0web，1移动
        :return:
        """
        url = self.host + "/chat-set/rest/selectConfigInfo/4"
        params = {
            "channelType": channelType,
            "current": 1,
            "pageSize": 100,
            "pageNo": 1
        }
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.get(url=url, headers=headers, params=params)
        print(f"\n response 的值为》》》：{response.text}\n\n")
        try:
            channelFlag_list = [child_source_info.get("channelFlag") for child_source_info in
                                json.loads(response.text)["list"]]
            print(f"\nchannelFlag_list 的值为》》》：{channelFlag_list}\n\n")
            return channelFlag_list
        except Exception as e:
            channelFlag_list = []
            print(f"\ne 的值为{e}\n")
            print(f'\njson.loads(response.text)["list"] 的值为》》》：{json.loads(response.text)["list"]}\n')
            return channelFlag_list

    # 新增渠道
    def add_channel(self,channelName,channelType):
        '''
        :param channelName:
        :param channelType: 0：桌面网站；1：移动网站
        :return:
        '''
        url = self.host + "/chat-set/rest/insertConfigInfo/4"
        data = urlencode(
            {
                "departmentId": "",
                "channelName": channelName,
                "channelType": channelType,
                "managerType": "1",
                "channelScene": "0"
            }
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'bNo': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.post(url, headers=headers, data=data)
        print(f"\n\n>>>得到的渠道id 为：{json.loads(response.text).get('item').get('channelFlag')}<<<<\n\n")

    # 查询智能路由条数
    def get_all_route_list(self,srStatus=1,srId_list=None):
        url = self.host  + f"/chat-set/smartRoute/getAllRouteList/4?srStatus={srStatus}"
        headers = {
            'bno': self.bno,
            'temp-id':self.tempid
        }
        response = self.session.get(url, headers=headers)
        print(response.text)
        try:
            srId_list = [srId_info.get("srId") for srId_info in json.loads(response.text).get("items")]
            print(f"get_all_route_list  >>>>：{srId_list}")
            return srId_list
        except Exception as e:
            print(e)
            return srId_list

    def modify_route_status(self,srId=None,srStatus=0):
        url = self.host  + f"/chat-set/smartRoute/modifyRouteStatus/4"
        data = {
                   'srId':srId,
                    'srStatus':srStatus
        }
        headers = {
            'bno': self.bno,
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'temp-id': self.tempid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = self.session.post( url, headers=headers, data=data)
        print(response.text)


if __name__ == '__main__':
    pass
    # img_num = random.randint(1,31)
    # print(f"img_num 的值为：{img_num}")
    # file_content = (f"p{img_num}.jpg", open(DATA_PATH + fr"\imgs\p{img_num}.jpg", mode="rb"),'image/jpg')
    obj = ConsoleSetting()
    # obj.uploading_images(file_content=file_content)
    # obj.get_child_source(channelType=1)
    # obj.add_channel(channelName="随便",channelType="1")
    srId_list = obj.get_all_route_list()
    try:
        for i in range(len(srId_list)):
            obj.modify_route_status(srId_list[i])
    except Exception:
        print(f"srId_list  的值为{srId_list}")
