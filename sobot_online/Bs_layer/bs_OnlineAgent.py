# @Time : 2023/11/25 23:06
# @Author : 雷洋平
# @File : bs_OnlineAgent.py
# @Software: PyCharm
# @Function:控制台 设置
import requests, re, json
from urllib.parse import urlencode
from sobot_online.Bs_layer.bs_login import Login
from faker import Faker


class ConsoleSetting(Login):
    fake = Faker(locale="zh_CN")

    def __init__(self):
        super().__init__()

    def uploading_images(self, file_content=None):
        """
        上传图片
        :param file_content:
        :return:
        """
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

    def get_child_source(self, channelType=0, current=1, pageSize=1000, pageNo=1):
        """
        获取PC\h5 的所有子渠道
        :param pageNo:
        :param pageSize:
        :param current:
        :param channelType:
        :return:
        """
        url = self.host + "/chat-set/rest/selectConfigInfo/4"
        params = {
            "channelType": channelType,
            "current": current,
            "pageSize": pageSize,
            "pageNo": pageNo
        }
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
        }
        response = self.session.get(url=url, headers=headers, params=params)
        try:
            channel_info = json.loads(response.text)["list"]
            print(f"\nchannel_info 的值为》》》：{channel_info}\n\n")
            return channel_info
        except Exception as e:
            channel_info = []
            print(f"\ne 的值为{e}\n")
            print(f'\njson.loads(response.text)["list"] 的值为》》》：{json.loads(response.text)["list"]}\n')
            return channel_info

    def add_channel(self, channelName="新增渠道:" + fake.name(), channelType=0):
        """
        新增渠道
        :param channelName:
        :param channelType: 0：桌面网站；1：移动网站
        :return:
        """
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

    def modify_channel_info(self, configId, channel_id,channelName, channelScene=0, operateFlag=0, channelType=0,
                            channelMark=None, managerType=1, isTraceFlag=0):
        url = self.host + "/chat-set/rest/updateConfigInSettings/4"
        data = {
            "channelScene": channelScene,
            "operateFlag": operateFlag,
            "channelType": channelType,
            "configId": configId,
            "id": channel_id,
            "channelName": channelName,
            "channelMark": channelMark,
            "managerType": managerType,
            "isTraceFlag": isTraceFlag
        }
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'temp-id': self.tempid
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)

    def get_all_route_list(self, srStatus=1, srId_list=None):
        """
        查询智能路由条数
        :param srStatus:
        :param srId_list:
        :return:
        """
        url = self.host + f"/chat-set/smartRoute/getAllRouteList/4?srStatus={srStatus}"
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
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

    def modify_route_status(self, srId=None, srStatus=0):
        """
        修改智能路由状态
        :param srId:
        :param srStatus:
        :return:
        """
        url = self.host + f"/chat-set/smartRoute/modifyRouteStatus/4"
        data = {
            'srId': srId,
            'srStatus': srStatus
        }
        headers = {
            'bno': self.bno,
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'temp-id': self.tempid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)

    def add_quick_menu(self, menuName="菜单名称：" + fake.name(), exhibit=1, menuType=0,
                       menuPicUrl="https://img.sobot.com/console/common/res/openModal.png",
                       msgText=fake.text()):
        """
        添加快捷菜单
        :param menuName:
        :param exhibit:
        :param menuType:
        :param menuPicUrl:
        :param msgText:
        :return:
        """
        url = self.host + f"/chat-set/v6/menuConfig/addCusMenuConfig"
        json_data = {
            'menuName': menuName,
            'exhibit': exhibit,
            "menuType": menuType,
            "menuPicUrl": menuPicUrl,
            "msgText": msgText
        }
        headers = {
            'bno': self.bno,
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = self.session.post(url, headers=headers, json=json_data)
        print(response.text)

    def add_quick_menu_sche(self, schemeName="添加方案：" + fake.name(), sortNo=0):
        """
        添加快捷菜单方案
        :param schemeName:
        :param sortNo:
        :return:
        """
        url = self.host + f"/chat-set/v6/menuConfig/addCusMenuPlanConfig"
        json_data = {
            "schemeName": schemeName,
            "sortNo": sortNo
        }
        headers = {
            'bno': self.bno,
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = self.session.post(url, headers=headers, json=json_data)
        print(response.text)

    def del_quick_menu_sche(self, schemeId="95bc63d52bde427ca2beac423d65577c"):
        """
        删除快捷菜单方案
        :param schemeId:
        """
        url = self.host + f"/chat-set/v6/menuConfig/delCusMenuPlanConfigById"
        json_data = {
            "id": schemeId
        }
        headers = {
            'bno': self.bno,
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        }
        del_quick_menu_sche_response = self.session.post(url, headers=headers, json=json_data)
        print(del_quick_menu_sche_response.text)

    def service_list_today(self, serviceStatusParam='online', keyword="", sortKey='', sortWay='',
                           page=1, size=15, searchWay=2, groupIdsParam='', service_online_list=None):
        """
        查询在线客服
        :param service_online_list:
        :param serviceStatusParam: 客服状态
        :param keyword:
        :param sortKey:
        :param sortWay:
        :param page:
        :param size:
        :param searchWay:
        :param groupIdsParam:
        :return:
        """
        url = self.host + f"/chat-statistics/monitor/serviceListToday"
        headers = {
            'bno': self.bno,
            'temp-id': self.tempid
        }
        params = {
            'serviceStatusParam': serviceStatusParam,
            'keyword': keyword,
            'sortKey': sortKey,
            'sortWay': sortWay,
            'page': page,
            'size': size,
            'searchWay': searchWay,
            'groupIdsParam': groupIdsParam,
        }
        response = self.session.get(url, headers=headers, params=params)
        if json.loads(response.text).get('items'):
            service_online_list = [serviceid.get('staffId') for serviceid in json.loads(response.text).get('items')]
            print(f'service_online_list>>>:{service_online_list}')
            return service_online_list
        else:
            return service_online_list

    def batch_offline_admin(self, adminIds='58832ae6f2434253be65ca18031f5ec8'):
        url = self.host + f"/chat-web/data/batchOfflineAdmin.action"
        json_data = {
            "adminIds": adminIds
        }
        headers = {
            'bno': self.bno,
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'temp-id': self.tempid,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = self.session.post(url, headers=headers, data=json_data)
        print(response.text)


if __name__ == '__main__':
    pass
    obj = ConsoleSetting()
    channelType=0
    channelid_info_list = obj.get_child_source(channelType=channelType)
    channelid_flag = [channelid.get('channelFlag') for channelid in channelid_info_list]
    print(f"channelid_flag>>>：{sorted(channelid_flag)}")

    # # 修改渠道信息
    # channelid_configId = [channelid.get('configId') for channelid in channelid_info_list]
    # channel_id = [channelid.get('id') for channelid in channelid_info_list]
    # for i in range(len(channelid_flag)-1):
    #     channelidflag = channelid_flag[i]
    #     configId = channelid_configId[i]
    #     channel_id = channelid_configId[i]
    #     obj.modify_channel_info(configId=configId, channel_id=channel_id,channelName='移动网站-'+str(channelidflag),channelType=channelType)

