import requests


def create_client():
    """创建多个用户"""
    for x in range(0, 60):
        init_url = "https://api-c.sobot.com/text/chat-visit/user/init.action"
        init_payload = {
            "sysNum": "fc3bcb5954a84c6aa1de6c13faecc079",  # 公司id
            "partnerId": "admin" + str(x),
            "source": 0
        }
        print(init_payload)
        res1 = requests.post(init_url, init_payload)
        uid = res1.json()["uid"]
        url = "https://api-c.sobot.com/text/chat-web/user/chatconnect.action"
        payload = {
            "sysNum": "cfd4681074ce4bed904928fb609fc824",  # 公司id
            "uid": uid,
            "groupId": "c7366a469ac5483cabdb03dc40513107",  # 技能组id
            "way": 1
        }
        res2 = requests.post(url, payload)
        print(res2.text)


if __name__ == '__main__':
    q = create_client()
