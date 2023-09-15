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
        serviceId = WorkBranch().service_menus()
        tid = WorkBranch().get_tid(serviceId)
        while True:
            if j <= 2:
                partnerid = "Admin" + str(random.randint(10000, 99999))
                uid, cid = Customer().customer_info_init(partnerid=partnerid)
                puid = Customer().chat_connection(uid, cid)
                while True:
                    if i <= 5:
                        time.sleep(1)
                        customer_content = self.Fk.text()
                        workbranch_content = self.Fk.paragraph()
                        Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid, content=customer_content)
                        WorkBranch().send_msg_to_customer(tid=tid, uid=uid, cid=cid, content=workbranch_content)
                        i += 1
                        # print(f"i 的值为{i}")
                        # print(f"customer_content 的值为{customer_content}")
                        # print(f"workbranch_content 的值为{workbranch_content}")
                    else:
                        Customer().out_action(uid=uid)
                        break
                j += 1
            else:
                WorkBranch().service_out(uid=tid)
                break


if __name__ == '__main__':
    pass
    obj01 = Interrelation()
    obj01.interrelation()
