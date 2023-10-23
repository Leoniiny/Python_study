# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服-客户相互联系
from faker import Faker
from sobot_online.Send_messages_to_each_other.Guest_side import *
from sobot_online.Send_messages_to_each_other.work_branch import *


class Interrelation:
    def __init__(self):
        self.Fk = Faker(locale="zh_CN")
        self.WK = WorkBranch()
        self.serviceId = self.WK.service_menus()
        self.tid = self.WK.get_tid(self.serviceId)
        # 登录客服工作台，保持客服在线
        self.WK.login_workbranche(self.tid)
        self.person_num = 5      # 进线客户数
        self.interrelation_num = 10      # 相互交互次数
        # print(f"self.serviceId >>>>：{self.serviceId}")
        # print(f"self.tid >>>>：{self.tid}")

    def interrelation(self):
        j = m = 1
        while True:
            if j <= self.person_num:
                print(f"这是第{j}个客户")
                j += 1
                partnerid = "admin" + str(random.randint(10000, 99999))
                uid, cid = Customer().customer_info_init(partnerid=partnerid,channelFlag="11")
                rest = Customer().chat_connection(uid=uid, cid=cid)
                puid = rest.get("puid")
                status = rest.get("status")
                print(f"走分支前的：puid >>>>：{puid},status >>>>：{status}")
                if status == 1:
                    i = 1
                    print(f"走的是status == 1 的分支")
                    while True:
                        if i <= self.interrelation_num:
                            time.sleep(1)
                            customer_content = self.Fk.text()
                            workbranch_content = self.Fk.paragraph()
                            Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid, content=customer_content)
                            WorkBranch().send_msg_to_customer(tid=self.tid,uid=uid, cid=cid, content=workbranch_content)
                            i += 1
                        else:
                            Customer().out_action(uid=uid)
                            break
                elif status == 2:
                    i = 1
                    print(f"走的是status == 2 的分支")
                    while True:
                        if i <= self.interrelation_num:
                            time.sleep(1)
                            customer_content = self.Fk.text()
                            Customer().send_message_to_robot(uid=uid, cid=cid, requestText=customer_content)
                            i += 1
                        else:
                            Customer().out_action(uid=uid)
                            break
                elif status == 6:
                    print(f"最先走的是status == 6 的分支！！！")
                    groupId = rest.get("groupList")[0].get("groupId")
                    rest = Customer().chat_connection(uid=uid, cid=cid,groupId=groupId)
                    status = rest.get("status")
                    print(f"puid >>>>：{puid},status >>>>：{status}")
                    if status == 1:
                        i = 1
                        print(f"然后走的是status == 1 的分支")
                        while True:
                            if i <= self.interrelation_num:
                                time.sleep(1)
                                customer_content = self.Fk.text()
                                workbranch_content = self.Fk.paragraph()
                                Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid, content=customer_content)
                                WorkBranch().send_msg_to_customer(tid=self.tid,uid=uid, cid=cid, content=workbranch_content)
                                i += 1
                            else:
                                Customer().out_action(uid=uid)
                                break
                    elif status == 2:
                        i = 1
                        print(f"然后走的是status == 2 的分支")
                        while True:
                            if i <= self.interrelation_num:
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
    # 跑代码前先看看测试环境，然后数据量尽量不好超过150，会出现锁死现象
    pass
    # 修改配置文件
    for i in range(5,6):
        if i == 1:
            value = "AL"
        if i == 2:
            value = "TX"
        if i == 3:
            value = "XJP"
        if i == 4:
            value = "HK"
        if i == 5:
            value = "US"
        renewal_yaml(file_path=r'''/config_file/operation_config.yml''',key="config",value=value)
        obj01 = Interrelation()
        obj01.interrelation()

