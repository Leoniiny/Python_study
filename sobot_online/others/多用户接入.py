import requests
from urllib.parse import urlencode
from faker import Faker
from sobot_online.common.file_dealing import *
fake = Faker(locale="zh_CN")


class Chat:
    def __init__(self):
        pass

    @classmethod
    def chat(cls,host="https://api-c.sobot.com/text",
             sysNum="cfd4681074ce4bed904928fb609fc824",
             groupId="75e16546892a4c5fa9fe07bbf9763e3b",
             partnerId=None):
        url = host + "/chat-visit/user/init/v6"
        if partnerId is None:
            partnerId = "admin-ali--" + str(random.randint(10000, 99999))
        payload = f'sysNum={sysNum}&source=0&groupId={groupId}&uname={partnerId}&partnerId={partnerId}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        uid = response.json()["uid"]
        cid = response.json()["cid"]
        puid = response.json()["puid"]

        url = host + "/chat-web/user/chatconnect.action"
        payload = f'sysNum={sysNum}&uid={uid}&cid={cid}&chooseAdminId=&tranFlag=0&current=false&groupId={groupId}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded', }
        response1 = requests.request("POST", url, headers=headers, data=payload)
        print(f"response1   >>>>{response1.text}")

        for i in range(1, 5):
            time.sleep(0.5)
            content = fake.text() + fake.text()
            # time.sleep(30)  # 每隔30秒发送一条信息给客服
            url = host + "/chat-web/message/user/send.action"
            data = urlencode({
                "puid": str(puid),
                "cid": str(cid),
                "uid": str(uid),
                "content": content,
                "objMsgType": "",
                "msgType": "0",
                "fileName": "undefined"
            })
            headers = {
                'bno': sysNum,
                'content-type': 'application/x-www-form-urlencoded',
            }
            response = requests.post(url=url, headers=headers, data=data)
            print(f"这是第{i}次，访客端返回数据response.text>>>：{response.text}")
        return uid, cid, puid

    @classmethod
    def customer_out(cls,host, uid):
        """
        客户离线
        :param host:
        :param uid:
        :return:
        """
        url = host + "chat-web/user/out.action"
        payload = f'uid={uid}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)


if __name__ == '__main__':
    pass
    obj = Chat()
    env = "ALG"
    customer_detail = load_yaml_file(filepath=r"/config_file/customer_env.yml")[f"{env}"]
    print(f"customer_detail>>>：{customer_detail}")
    for i in range(10,23):
        obj.chat(
            host=customer_detail.get('host'),
            sysNum=customer_detail.get('sysNum'),
            groupId=customer_detail.get('groupId'),
            partnerId="receive" + str(i)
        )

