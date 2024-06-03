# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.Bs_layer.bs_GuestSide import *


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
    for i in range(6, 11):
        partnerid = 'ALGleavemsg-' + str(i)
        uname = '客户' + str(i)
        tel = str(random.randint(11111111,111111111))
        # 19, 20, 21, 22, 23, 24
        # 19, 20, 21, 22, 23, 24
        for j in range(20, 26):
            for k in range(1,3):
                if j % 2 == 1:
                    source = 4
                    isVip = '1'
                    content = f'这是移动渠道-{j}来的，这个客户{partnerid}的第{k}次留言'
                    obj.leave_msg(partnerid=partnerid, source=source, content=content, uname=uname,channelFlag=str(j),tel=tel,isVip=isVip)
                else:
                    source = 0
                    content = f'这是桌面网站-{j}来的，这个客户{partnerid}的第{k}次留言'
                    obj.leave_msg(partnerid=partnerid, source=source, content=content, uname=uname,channelFlag=str(j),tel=tel)
