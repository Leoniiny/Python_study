# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服-客户相互联系
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("root_path的值为：%s" % root_path)
sys.path.append(root_path)

from faker import Faker
from sobot_online.Send_messages_to_each_other.Guest_side import *
from sobot_online.Send_messages_to_each_other.work_branch import *
from sobot_online.Send_messages_to_each_other.console_setting import *


class Interrelation:
    def __init__(self):
        self.Fk = Faker(locale="zh_CN")
        self.WK = WorkBranch()
        self.serviceId = self.WK.service_menus()
        self.tid = self.WK.get_tid(self.serviceId)
        # 登录客服工作台，保持客服在线
        self.WK.login_workbranche(self.tid)
        self.person_num = 2  # 进线客户数
        self.interrelation_num = 2  # 相互交互次数
        # print(f"self.serviceId >>>>：{self.serviceId}")
        # print(f"self.tid >>>>：{self.tid}")

    # 客户与客服互相发消息
    def interrelation(self):
        j =0
        while True:
            j += 1
            isVip = questionStatus = score = solved = commentType = j % 2
            if j <= self.person_num:
                print(f"这是第{j}个客户")
                partnerid = "客户--"+self.Fk.name()+"--" + str(random.randint(100000,999999))
                uid, cid,pid = Customer().customer_info_init(partnerid=partnerid, source=str(random.randint(0,4)), channelFlag=str(random.randint(0,5)),isVip=str(isVip))
                chat_connection_rest = Customer().chat_connection(uid=uid, cid=cid)
                puid = chat_connection_rest.get("puid")
                status = chat_connection_rest.get("status")
                print(f"走分支前的：puid >>>>：{puid},status >>>>：{status}")
                if status == 1:
                    i = 1
                    print(f"查询status 之后，首先走的是status == 1 的分支")
                    while True:
                        if i <= self.interrelation_num:
                            time.sleep(1)
                            customer_content = self.Fk.text()
                            workbranch_content = self.Fk.paragraph()
                            Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid, content=customer_content)
                            WorkBranch().send_msg_to_customer(tid=self.tid, uid=uid, cid=cid,
                                                              content=workbranch_content)
                            i += 1
                        else:
                            # 客服邀请评价： commentType == 0 为客服邀请评价
                            if commentType == 0:
                                WorkBranch().recomment(tid=self.tid,cid=cid,uid=uid)
                            # 客服进行服务总结
                            fields_value = questionDescribe = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                            unit_info,unit_body_list,unit_fieldList = WorkBranch().get_unifo_body(tid=self.tid,cid=cid)
                            print(f"获取业务单元列表 unit_info >>>：{unit_info}，unit_body_list >>>：{unit_body_list},unit_fieldList >>>：{unit_fieldList}",sep="\n")
                            WorkBranch().submmit_summary(tid=self.tid,uid=uid,cid=cid,pid=pid,questionStatus=questionStatus,questionDescribe=questionDescribe,fields_value=fields_value,
                                                         unit_info=unit_info, unit_body_list=unit_body_list, unit_fieldList=unit_fieldList)
                            # 客户进行满意度评价
                            satisfaction_info = Customer().satisfaction_message_data(uid=uid)
                            Customer().comment(cid=cid,uid=uid,solved=solved,remark=self.Fk.text(),commentType=commentType,satisfaction_info = satisfaction_info)
                            print(f"评价成功！！！")
                            # 客户进行留言
                            Customer().allot_leave_msg(uid=uid, content=content)
                            Customer().out_action(uid=uid)
                            break
                elif status == 2:
                    i = 1
                    print(f"查询status 之后，首先走的是status == 2 的分支")
                    while True:
                        if i <= self.interrelation_num:
                            time.sleep(1)
                            customer_content = self.Fk.text()
                            Customer().send_message_to_robot(uid=uid, cid=cid, requestText=customer_content)
                            i += 1
                        else:
                            remark = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                            # 给机器人评价
                            Customer().comment(cid=cid, uid = uid,score=score, tag="回答错误",solved=solved, remark=remark, satisfy_type=0,commentType="1",scoreFlag=0, scoreExplain="",satisfaction_info=None)
                            # 给机器人留言
                            Customer().allot_leave_msg(uid=uid, content=content)
                            Customer().out_action(uid=uid)
                            break
                elif status == 6:
                    print(f"查询status 之后，首先走的是status == 6 的分支,然后去获取技能组id")
                    groupId = chat_connection_rest.get("groupList")[0].get("groupId")
                    # 通过groupid 获取新的客服工作状态
                    chat_connection_rest_bygroupid = Customer().chat_connection(uid=uid, cid=cid, groupId=groupId)
                    status = chat_connection_rest_bygroupid.get("status")
                    print(f"status == 6 >>>   puid >>>：{puid},status >>>>：{status}")
                    if status == 1:
                        i = 1
                        print(f"查询status 之后，首先走的是status == 1 的分支")
                        while True:
                            if i <= self.interrelation_num:
                                time.sleep(1)
                                customer_content = self.Fk.text()
                                workbranch_content = self.Fk.paragraph()
                                Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid,
                                                                      content=customer_content)
                                WorkBranch().send_msg_to_customer(tid=self.tid, uid=uid, cid=cid,
                                                                  content=workbranch_content)
                                i += 1
                            else:
                                # 客服邀请评价： commentType == 0 为客服邀请评价
                                if commentType == 0:
                                    WorkBranch().recomment(tid=self.tid, cid=cid, uid=uid)
                                # 客服进行服务总结
                                fields_value = questionDescribe = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                                unit_info, unit_body_list, unit_fieldList = WorkBranch().get_unifo_body(tid=self.tid,
                                                                                                        cid=cid)
                                print(
                                    f"获取业务单元列表 unit_info >>>：{unit_info}，unit_body_list >>>：{unit_body_list},unit_fieldList >>>：{unit_fieldList}",
                                    sep="\n")
                                WorkBranch().submmit_summary(tid=self.tid, uid=uid, cid=cid, pid=pid,
                                                             questionStatus=questionStatus,
                                                             questionDescribe=questionDescribe,
                                                             fields_value=fields_value,
                                                             unit_info=unit_info, unit_body_list=unit_body_list,
                                                             unit_fieldList=unit_fieldList)
                                # 客户进行满意度评价
                                satisfaction_info = Customer().satisfaction_message_data(uid=uid)
                                Customer().comment(cid=cid, uid=uid, solved=solved, remark=self.Fk.text(),
                                                   commentType=commentType, satisfaction_info=satisfaction_info)
                                print(f"评价成功！！！")
                                # 客户进行留言
                                Customer().allot_leave_msg(uid=uid, content=content)
                                Customer().out_action(uid=uid)
                                break
                    elif status == 2:
                        i = 1
                        print(f"status节点 6 》 2")
                        while True:
                            if i <= self.interrelation_num:
                                time.sleep(1)
                                customer_content = self.Fk.text()
                                Customer().send_message_to_robot(uid=uid, cid=cid, requestText=customer_content)
                                i += 1
                            else:
                                remark = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                                # 给机器人评价
                                Customer().comment(cid=cid, uid = uid,score=score, tag="回答错误",solved=solved, remark=remark, satisfy_type=0,commentType="1",scoreFlag=0, scoreExplain="",satisfaction_info=None)
                                # 给机器人留言
                                Customer().allot_leave_msg(uid=uid, content=content)
                                Customer().out_action(uid=uid)
                                break
            else:
                break


if __name__ == '__main__':
    # 跑代码前先看看测试环境，然后数据量尽量不好超过150，会出现锁死现象
    pass
    # 修改配置文件
    for i in range(1, 2):
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
        renewal_yaml(file_path=r'''/config_file/operation_config.yml''', key="config", value=value)
        obj01 = Interrelation()
        obj01.interrelation()
