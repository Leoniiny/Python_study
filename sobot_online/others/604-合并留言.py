# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.Bs_layer.bs_GuestSide import *
from faker import Faker
from sobot_online.Bs_layer.bs_OnlineAgent import *

fake = Faker(locale="zh")


class Merge_leavMsg(Customer):
    def __init__(self):
        super().__init__()

    def leave_msg(self, partnerid=None, source=0, content='aaa', uname='',channelFlag='',tel="",isVip=''):
        info_group = super().v2_customer_info_init(partnerid=partnerid, source=source, uname=uname, channelFlag=channelFlag,tel=tel,isVip=isVip)
        uid = info_group[0]
        print(f"uid的值为：{uid}")
        super().allot_leave_msg(uid, content=content)
        super().out_action(uid)


if __name__ == '__main__':
    obj = Merge_leavMsg()
    for i in range(1, 5):
        partnerid = "testleave"+str(random.randint(1111111, 999999999))
        content = f'这个客户{partnerid}的留言'
        obj.leave_msg(partnerid=partnerid, source=0, content=content)
    rest = ConsoleSetting().leavemsg_list()
    if rest.get('items'):
        currentAdminName_list =[]
        for i in range(1, 5):
            currentAdminName_list.append(rest.get('items')[i-1].get('currentAdminName'))
        print(currentAdminName_list)


    # for i in range(16, 21):
    #     partnerid = 'ALGleavemsg-' + str(i)
    #     uname = '客户' + str(i)
    #     tel = str(random.randint(1111111,999999999))
    #     # 50, 51, 52, 53, 54, 55, 56, 57
    #     # 50, 51, 52, 53, 54, 55, 56, 57
    #     # 新加坡：16, 17, 18, 19, 20, 21
    #     # 32, 33, 34, 35, 36, 37, 38, 39
    #     for j in range(32, 36):
    #         # 子渠道
    #         for k in range(1,3):
    #             if j % 2 == 1:
    #                 source = 4
    #                 isVip = '1'
    #                 content = f'这是移动渠道-{j}来的，这个客户{partnerid}的第{k}次留言'
    #                 obj.leave_msg(partnerid=partnerid, source=source, content=content, uname=uname,channelFlag=str(j),tel=tel,isVip=isVip)
    #             else:
    #                 source = 0
    #                 content = f'这是桌面网站-{j}来的，这个客户{partnerid}的第{k}次留言'
    #                 obj.leave_msg(partnerid=partnerid, source=source, content=content, uname=uname,channelFlag=str(j),tel=tel)
