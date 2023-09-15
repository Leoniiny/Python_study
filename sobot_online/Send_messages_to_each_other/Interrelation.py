# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服-客户相互联系
import time
from faker import Faker

from sobot_online.Send_messages_to_each_other.Guest_side import *
from sobot_online.Send_messages_to_each_other.work_branch import *


class Interrelation:
    def __init__(self):
        self.Fk = Faker(locale="zh_CN")

    def interrelation(self):
        i = j = m = 0
        uid,cid = Customer().customer_info_init()
        puid = Customer().chat_connection(uid = uid,cid = cid)
        while True:
            if i <= 5:
                time.sleep(1)
                customer_content = self.Fk.text()
                workbranch_content = self.Fk.paragraph()
                Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid, content=customer_content)
                WorkBranch().send_msg_to_customer(uid=uid, cid=cid, content=workbranch_content)
                i += 1
            else:
                Customer().out_action(uid=uid)
                break


if __name__ == '__main__':
    pass
    obj01 = Interrelation()
    obj01.interrelation()
