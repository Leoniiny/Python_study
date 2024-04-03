import time

import requests
from urllib.parse import urlencode
for i in range(29,200):
    time.sleep(0.5)
    url = "https://test-branche1.sobot.com/text/chat-set/rest/insertConfigInfo/4"
    data = urlencode(
        {"departmentId": "",
         "channelName": f"移动网站渠道{i}",
         "channelType": "1",    #1 为移动网站
         "managerType": "1",
         "channelScene": "0"
         }
    )
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': 'https://console.sobot.com',
      'Referer': 'https://console.sobot.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
      'bNo': 'cfd4681074ce4bed904928fb609fc824',
      'language': 'zh',
      'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'temp-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI0NDNhZjdhZmEyM2Y0Yzg3YTg5MDBmMTc4MTM3ZDA5YyIsImFnZW50SWQiOiJjNjE0NTZmNzVjYmY0M2ZkYjA5ODBjMzdhNGYyYjQ5YyIsInNlcnZpY2VFbWFpbCI6ImNzeGIwMUBxcS5jb20iLCJ6b25lIjowLCJpc3MiOiJjc3hiMDFAcXEuY29tIiwiZXhwIjoxNzEyMTMxMjcwLCJ0eXBlIjoiY29uc29sZSJ9.V66a53NjvSO7oZcqnydnf31fkMej2II8oiMCzdJuers',
    'timezone': '+08:00',
      'timezoneid': 'Asia/Shanghai'
    }

    response = requests.request("POST", url, headers=headers, data=data)

    print(response.text)
