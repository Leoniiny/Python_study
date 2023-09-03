import json
import requests
from urllib.parse import urlencode

def out_action():
    url = "http://hk.sobot.com/chat-web/user/out.action"
    data = {"uid": "e26b9ec6eeaf1d491470315b98e55810"}
    headers = {
        'bno': '913d909e3a194598ba61cf904b5dc12a',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)


if __name__ == '__main__':
    obj = out_action()
