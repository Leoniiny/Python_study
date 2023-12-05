import json
import time
import requests, random
from urllib.parse import urlencode
from faker import Faker

fake = Faker(locale="zh_CN")


def died_data(
        host="https://api-c.sobot.com/text",
        sysNum="cfd4681074ce4bed904928fb609fc824",
        groupId="c360e6dfc43d4cbbb232a8ab215a535e"):
    url = host + "/chat-visit/user/init/v6"
    partnerId = "admin-ali--" + str(random.randint(10000, 99999))
    payload = f'sysNum={sysNum}&source=0&groupId={groupId}&uname={partnerId}&partnerId={partnerId}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    uid = response.json()["uid"]
    cid = response.json()["cid"]
    puid = response.json()["puid"]

    url = host + "/chat-web/user/chatconnect.action"
    payload = f'sysNum={sysNum}&uid={uid}&cid={cid}&chooseAdminId=&tranFlag=0&current=false&groupId={groupId}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded', }
    response1 = requests.request("POST", url, headers=headers, data=payload)
    print(f"response1   >>>>{response1.text}")

    for i in range(1, 10):
        time.sleep(0.5)
        content = fake.text() + fake.text() + fake.text() + fake.text() + fake.text() + fake.text()
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
        response = requests.post(url, headers=headers, data=data)
        print(f"puid>>>：{puid}, uid>>>:{uid}, cid>>>:{cid}")
        print(f"访客端返回数据response.text>>>:{response.text}")


if __name__ == '__main__':
    pass
    m = 0
    while True:
        if m <= 10:
            for i in range(30):
                died_data()
            time.sleep(600)
            m += 1
        else:
            break
