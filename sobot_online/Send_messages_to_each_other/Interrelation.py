# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服-客户相互联系
from faker import Faker

from sobot_online.Send_messages_to_each_other.Guest_side import *
from sobot_online.Send_messages_to_each_other.work_branch import *


class Interrelation:
    def __init__(self):
        self.Fk = Faker(locale="zh_CN")

    def interrelation(self):
        i = j = m = 0
        while True:
            if j <= 2:
                j += 1
                partnerid = "admin" + str(random.randint(10000, 99999))
                uid, cid = Customer().customer_info_init(partnerid=partnerid)
                puid, status = Customer().chat_connection(uid=uid, cid=cid)
                print(f"puid >>>>：{puid},status >>>>：{status}")
                if status == 1:
                    i = 1
                    print(f"走的是status == 1 的分支")
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
                elif status == 2:
                    i = 1
                    print(f"走的是status == 2 的分支")
                    while True:
                        if i <= 5:
                            time.sleep(1)
                            customer_content = self.Fk.text()
                            Customer().send_message_to_robot(uid=uid, cid=cid, requestText=customer_content)
                            i += 1
                        else:
                            Customer().out_action(uid=uid)
                            break
            else:
                break


if __name__ == '__main__':
    pass
    obj01 = Interrelation()
    obj01.interrelation()
