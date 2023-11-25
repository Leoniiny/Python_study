# @Time : 2023/11/25 23:06
# @Author : 雷洋平
# @File : console_setting.py
# @Software: PyCharm
# @Function:控制台 设置


# import os
# import sys
#
# root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print("root_path的值为：%s" % root_path)
# sys.path.append(root_path)

from sobot_online.Send_messages_to_each_other.work_branch import WorkBranch
from sobot_online.common.file_dealing import *
import json, re


class ConsoleSetting(WorkBranch):
    def __init__(self):
        super().__init__()

    # 上传图片
    def uploading_images(self,file_content=None):
        url = self.host + "/chat-web/webchat/expressionUpload"
        data = {
            "pid": self.bno,
        }
        files = {
            "file": file_content
        }
        headers = {
            "Temp-Id":self.tempid
        }
        response = self.session.post(url = url,headers = headers,data=data,files=files)
        img_url = ""
        try:
            img_url = json.loads(response.text).get("item").get("url")
            return img_url
        except Exception as e:
            print(f"\n response 的结果为：{json.loads(response.text)}；\n\ne 的返回值为：{e}；\n")
            return img_url


if __name__ == '__main__':
    pass
    img_num = random.randint(1,31)
    print(f"img_num 的值为：{img_num}")
    file_content = (f"p{img_num}.jpg", open(DATA_PATH + fr"\imgs\p{img_num}.jpg", mode="rb"),'image/jpg')
    obj = ConsoleSetting()
    obj.uploading_images(file_content=file_content)