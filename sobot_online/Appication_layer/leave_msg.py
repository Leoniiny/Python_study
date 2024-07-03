# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.Bs_layer.bs_OnlineAgent import *


class LeaveMsg(ConsoleSetting):
    def __init__(self):
        super().__init__()

    def multi_modify_info(self,channelType=0):
        channelid_info_list = obj.get_child_source(channelType=channelType)
        channelid_flag = [channelid.get('channelFlag') for channelid in channelid_info_list]
        print(f"channelid_flag>>>：{sorted(channelid_flag)}")

        # 修改渠道信息
        if channelType == 0 :
            channelName = '桌面网站-'
        else:
            channelName = '移动网站-'
        channelid_configId = [channelid.get('configId') for channelid in channelid_info_list]
        for i in range(len(channelid_flag) - 1):
            channelidflag = channelid_flag[i]
            configId = channelid_configId[i]
            channel_id = channelid_configId[i]
            obj.modify_channel_info(configId=configId, channel_id=channel_id, channelName=channelName + str(channelidflag),
                                    channelType=channelType)