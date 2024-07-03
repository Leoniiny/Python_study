# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：客服-客户相互联系
# linux 下的路径只能是 /
import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("root_path的值为：%s" % root_path)
sys.path.append(root_path)

from faker import Faker
from sobot_online.Bs_layer.bs_GuestSide import Customer
from sobot_online.Bs_layer.bs_WorkBranche import WorkBranch
from sobot_online.Bs_layer.bs_CRM import CRM
from sobot_online.common.file_dealing import *


class Interrelation(WorkBranch, Customer):
    def __init__(self, person_num=1, interrelation_num=2):
        super().__init__()
        if self.sb in ["AL", "TX","TS"]:
            self.Fk = Faker(locale="zh_CN")
            self.vist_name = "访客"
        else:
            self.Fk = Faker(locale="en_GB")
            self.vist_name = "visitor"
        self.serviceId = super().service_menus()
        self.tid = super().get_tid(self.serviceId)
        service_online_list = super().service_list_today()
        if service_online_list:
            for serviceid in service_online_list:
                super().batch_offline_admin(adminIds=serviceid)
        # 登录客服工作台，保持客服在线
        super().login_workbranche(self.tid)
        self.person_num = person_num  # 进线客户数
        self.interrelation_num = interrelation_num  # 相互交互次数

    # 客户与客服互相发消息
    def interrelation(self):
        j = 0
        while True:
            # j 确定是第几个人进线
            j += 1
            if j <= self.person_num:
                # 初始化访客进线信息
                print(f"这是第{j}个客户;当前运行的是域名是：{self.host}")
                face_num = isVip = questionStatus = score = solved = commentType = j % 2
                source = random.choice([0, 4])
                print(f"\n\nsource 的值为  >>>>：{source}\n\n")
                channelFlag = ''
                if source == 4:
                    channelFlag_info_list = super().get_child_source(channelType=1)
                else:
                    channelFlag_info_list = super().get_child_source(channelType=source)
                if channelFlag_info_list:
                    channelFlag_list = [channel_info.get('channelFlag') for channel_info in channelFlag_info_list]
                    if len(channelFlag_list) < 15:
                        channel_name = self.Fk.name() + str(random.randint(100, 999))
                        if source == 4:
                            super().add_channel(channelName=channel_name, channelType=1)
                        else:
                            super().add_channel(channelName=channel_name, channelType=source)
                    if channelFlag_list:
                        channelFlag = random.choice(channelFlag_list)
                        print(f"\n\nchannelFlag 的值为  >>>>：{channelFlag}\n\n")
                if face_num == 1:
                    img_num = random.randint(1, 30)
                    file_content = (
                        f"p{img_num}.jpg", open(DATA_PATH + fr"/imgs/p{img_num}.jpg", mode="rb"), 'image/jpg'
                    )
                    face = super().uploading_images(file_content=file_content)
                else:
                    face = ""
                # partnerid = "test" + str(random.randint(100000, 999999))
                partnerid = "satis" + str(random.randint(10, 99))
                uname = self.vist_name + "：" + self.Fk.name() + "-" + partnerid
                email_num = self.Fk.company_email()
                tel = self.Fk.phone_number()
                # 确定客户信息初始化
                uid, cid, pid,userId = super().v2_customer_info_init(partnerid=partnerid, uname=uname,
                                                                     source=source, face=face, email_num=email_num, tel=tel,
                                                                     channelFlag=channelFlag, isVip=str(isVip))
                # 关闭智能路由
                srId_list = super().get_all_route_list()
                try:
                    for i in range(len(srId_list)):
                        super().modify_route_status(srId_list[i])
                except Exception:
                    print(f"srId_list  的值为{srId_list}")
                # 访客进线
                chat_connection_rest = super().chat_connection(uid=uid, cid=cid)
                puid = chat_connection_rest.get("puid")
                status = chat_connection_rest.get("status")
                print(f"\n\n走分支前的：puid >>>>：{puid},status >>>>：{status}\n\n")
                if status == 1:
                    i = 1
                    print(f"\n\n查询status 之后，首先走的是status == 1 的分支\n\n")
                    while True:
                        if i <= self.interrelation_num:
                            # reply_time = random.randint(1, 5)
                            reply_time = 1
                            print(f"\n\nreply_time 的值为{reply_time}\n\n")
                            time.sleep(reply_time)
                            customer_content = self.Fk.text()
                            workbranch_content = self.Fk.paragraph()
                            Customer().send_message_to_workbranch(puid=puid, uid=uid, cid=cid, content=customer_content)
                            time.sleep(reply_time)
                            super().send_msg_to_customer(tid=self.tid, uid=uid, cid=cid,
                                                         content=workbranch_content)
                            i += 1
                        else:
                            # 客服邀请评价： commentType == 0 为客服邀请评价
                            if commentType == 0:
                                super().recomment(tid=self.tid, cid=cid, uid=uid)
                            # 客服进行服务总结
                            fields_value = questionDescribe = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                            unit_info, unit_body_list, unit_fieldList = super().get_unifo_body(tid=self.tid, cid=cid)
                            print(f"\n获取业务单元列表 unit_info >>>：{unit_info}，unit_body_list >>>：{unit_body_list}"
                                  f",unit_fieldList >>>：{unit_fieldList}\n", sep="\n")
                            super().submmit_summary(tid=self.tid, uid=uid, cid=cid, pid=pid,
                                                    questionStatus=questionStatus, questionDescribe=questionDescribe,
                                                    fields_value=fields_value,
                                                    unit_info=unit_info, unit_body_list=unit_body_list,
                                                    unit_fieldList=unit_fieldList)
                            # 客户进行满意度评价
                            satisfaction_info = super().satisfaction_message_data(uid=uid)
                            super().comment(cid=cid, uid=uid, solved=solved, remark=self.Fk.text(),
                                            commentType=commentType, satisfaction_info=satisfaction_info)
                            print(f"\n\n客户进行满意度评价 评价成功！！！\n\n")
                            # 客户进行留言
                            super().allot_leave_msg(uid=uid, content=content)
                            # 访客离线
                            super().out_action(uid=uid)
                            break
                elif status == 2:
                    i = 1
                    print(f"\n\n查询status 之后，首先走的是status == 2 的分支\n\n")
                    while True:
                        if i <= self.interrelation_num:
                            time.sleep(1)
                            customer_content = self.Fk.text()
                            super().send_message_to_robot(uid=uid, cid=cid, requestText=customer_content)
                            i += 1
                        else:
                            remark = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                            # 给机器人评价
                            super().comment(cid=cid, uid=uid, score=score, tag="回答错误", solved=solved, remark=remark,
                                            satisfy_type=0, commentType="1", scoreFlag=0, scoreExplain="",
                                            satisfaction_info=None)
                            # 给机器人留言
                            super().allot_leave_msg(uid=uid, content=content)
                            super().out_action(uid=uid)
                            break
                elif status == 6:
                    print(f"\n\n查询status 之后，首先走的是status == 6 的分支,然后去获取技能组id\n\n")
                    groupId = chat_connection_rest.get("groupList")[0].get("groupId")
                    # 通过groupid 获取新的客服工作状态
                    chat_connection_rest_bygroupid = Customer().chat_connection(uid=uid, cid=cid, groupId=groupId)
                    status = chat_connection_rest_bygroupid.get("status")
                    print(f"\n\nstatus == 6 >>>   puid >>>：{puid},status >>>>：{status}\n\n")
                    if status == 1:
                        i = 1
                        print(f"\n\n查询status 之后，首先走的是status == 1 的分支\n\n")
                        while True:
                            if i <= self.interrelation_num:
                                # reply_time = random.randint(1, 5)
                                reply_time = 1
                                print(f"\n\nreply_time 的值为{reply_time}\n\n")
                                customer_content = self.Fk.text()
                                workbranch_content = self.Fk.paragraph()
                                time.sleep(reply_time)
                                super().send_message_to_workbranch(puid=puid, uid=uid, cid=cid,
                                                                   content=customer_content)
                                time.sleep(reply_time)
                                super().send_msg_to_customer(tid=self.tid, uid=uid, cid=cid,
                                                             content=workbranch_content)
                                i += 1
                            else:
                                # 客服邀请评价： commentType == 0 为客服邀请评价
                                if commentType == 0:
                                    super().recomment(tid=self.tid, cid=cid, uid=uid)
                                # 客服进行服务总结
                                fields_value = questionDescribe = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                                unit_info, unit_body_list, unit_fieldList = super().get_unifo_body(tid=self.tid,
                                                                                                   cid=cid)
                                print(
                                    f"\n\n获取业务单元列表 unit_info >>>：{unit_info}，unit_body_list >>>：{unit_body_list},unit_fieldList >>>：{unit_fieldList}\n\n")
                                super().submmit_summary(tid=self.tid, uid=uid, cid=cid, pid=pid,
                                                        questionStatus=questionStatus,
                                                        questionDescribe=questionDescribe,
                                                        fields_value=fields_value,
                                                        unit_info=unit_info, unit_body_list=unit_body_list,
                                                        unit_fieldList=unit_fieldList)
                                # 客户进行满意度评价
                                satisfaction_info = super().satisfaction_message_data(uid=uid)
                                super().comment(cid=cid, uid=uid, solved=solved, remark=self.Fk.text(),
                                                commentType=commentType, satisfaction_info=satisfaction_info)
                                print(f"\n\n  6 --->> 1  客户进行满意度评价评价成功！！！\n\n")
                                # 客户进行留言
                                super().allot_leave_msg(uid=uid, content=content)
                                super().out_action(uid=uid)
                                break
                    elif status == 2:
                        i = 1
                        print(f"\n\nstatus节点 6 》 2\n\n")
                        while True:
                            if i <= self.interrelation_num:
                                time.sleep(1)
                                customer_content = self.Fk.text()
                                super().send_message_to_robot(uid=uid, cid=cid, requestText=customer_content)
                                i += 1
                            else:
                                remark = content = self.Fk.paragraph() + self.Fk.paragraph() + self.Fk.paragraph()
                                # 给机器人评价
                                super().comment(cid=cid, uid=uid, score=score, tag="回答错误", solved=solved,
                                                remark=remark, satisfy_type=0, commentType="1", scoreFlag=0,
                                                scoreExplain="", satisfaction_info=None)
                                # 给机器人留言
                                super().allot_leave_msg(uid=uid, content=content)
                                super().out_action(uid=uid)
                                break
            else:
                # 工作台离线
                super().service_out(uid = self.tid)
                print(f"当前运行的是域名是：{self.host}")
                time.sleep(5)
                break


if __name__ == '__main__':
    # 跑代码前先看看测试环境，然后数据量尽量不好超过150，会出现锁死现象
    pass
    # 修改配置文件
    person_num = random.randint(4, 11)
    interrelation_num = random.randint(1, 10)
    print(f"\n\nperson_num >>>：{person_num},interrelation_num >>>：{interrelation_num},\n\n")
    value = "TS"
    # for i in range(4, 5):
    #     if i == 1:
    #         value = "AL"
    #     if i == 2:
    #         value = "TX"
    #     if i == 3:
    #         value = "XJP"
    #     if i == 4:
    #         value = "HK"
    #     if i == 5:
    #         value = "US"
    #     if i == 6:
    #         value = "TS"
    #     if i == 7:
    #         value = "ALG"
    renewal_yaml(file_path=r'''/config_file/operation_config.yml''', key="config", value=value)
    obj01 = Interrelation(person_num=10, interrelation_num=2)
    if obj01.tempid is not None:
        obj01.interrelation()
    else:
        pass
