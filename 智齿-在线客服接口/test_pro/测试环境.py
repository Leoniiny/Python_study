import requests


def create_client():
    """创建多个用户"""
    for x in range(0, 60):
        init_url = "http://test.sobot.com/chat-visit/user/init.action"
        init_payload = {
            "sysNum": "fc3bcb5954a84c6aa1de6c13faecc079",  # 公司id
            "partnerId": "admin" + str(x),
            "source": 0
        }
        print(init_payload)
        res1 = requests.post(init_url, init_payload)
        uid = res1.json()["uid"]
        url = "http://test.sobot.com/chat-web/user/chatconnect.action"
        payload = {
            "sysNum": "fc3bcb5954a84c6aa1de6c13faecc079",  # 公司id
            "uid": uid,
            "groupId": "edb91537dbfd4ca084faf93cb6e83c57",  # 技能组id
            "way": 1
        }
        res2 = requests.post(url, payload)
        print(res2.text)


if __name__ == '__main__':
    q = create_client()
