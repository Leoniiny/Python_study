# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.Bs_layer.bs_GuestSide import *


class Merge_leavMsg(Customer):
    def __init__(self):
        super().__init__()

    def leave_msg(self, partnerid=None, source=0, content='aaa', uname='',channelFlag=''):
        info_group = super().customer_info_init(partnerid=partnerid, source=source, uname=uname,channelFlag=channelFlag)
        uid = info_group[0]
        print(f"uid的值为：{uid}")
        super().allot_leave_msg(uid, content=content)
        super().out_action(uid)


if __name__ == '__main__':
    obj = Merge_leavMsg()
    for i in range(30, 31):
        partnerid = 'leavmsg' + str(i)
        uname = '客户' + str(i)
        for j in range(19, 21):
            for k in range(1,3):
                if j % 2 == 1:
                    source = 4
                    content = f'这是移动渠道来的，这个客户{partnerid}的第{k}次留言'
                    obj.leave_msg(partnerid=partnerid, source=source, content=content, uname=uname,channelFlag=str(j))
                else:
                    source = 0
                    content = f'这是桌面网站来的，这个客户{partnerid}的第{k}次留言'
                    obj.leave_msg(partnerid=partnerid, source=source, content=content, uname=uname,channelFlag=str(j))
