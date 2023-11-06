import requests


def create_client():
    """创建多个用户"""
    for x in range(57, 100):
        # init_url = "https://api-c.soboten.com/text/chat-visit/user/init.action"
        # init_url = "https://www.sobot.com/chat-visit/user/init.action"
        init_url = "https://test-branche1.sobot.com/text/chat-visit/user/init/v6"
        # init_url = "https://sg.sobot.com/chat-visit/user/init.action"
        init_payload = {
            "sysNum": "443af7afa23f4c87a8900f178137d09c",  # 公司id
            "partnerId": "admin" + str(x),
            "source": 4
        }
        print(init_payload)
        res1 = requests.post(init_url, init_payload)
        uid = res1.json()["uid"]
        # url = "https://api-c.soboten.com/text/chat-web/user/chatconnect.action"
        url = "https://test-branche1.sobot.com/text/chat-web/user/chatconnect.action"
        # url = "https://www.soboten.com/chat-web/user/chatconnect.action"
        # url = "https://sg.sobot.com/chat-web/user/chatconnect.action"
        payload = {
            "sysNum": "443af7afa23f4c87a8900f178137d09c",  # 公司id
            # 阿里云：150d6fa1252f482094b708f2b19a1bb1
            # 腾讯云：5105b359aa37444284f5b0660a6fed24
            # 测试环境：443af7afa23f4c87a8900f178137d09c
            # 香港：913d909e3a194598ba61cf904b5dc12a
            "uid": uid,
            "groupId": "02aef73af7374cddae8dc639f71b8f24",  # 技能组id
            # 腾讯云：c0ea210d47a945fbb125deddd245d602
            # 阿里云：7c52b375120a4c9599cf046f2742afdc
            # 测试环境：6b8f4ac453504cb1ba7ad10a20124f4f
            # 香港环境：18634c519b134cce9cd3a663297ba9e9
            "way": 1
        }
        res2 = requests.post(url, payload)
        print(res2.text)


if __name__ == '__main__':
    q = create_client()
