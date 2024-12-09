# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from urllib.parse import urlencode

import requests
def get_agent_info():
    agent_list =[]
    for i in range(1, 4):
        url = "https://api-c-grey.sobot.com/text/basic-public/agent/queryDepartAgentInfoList"
        data ={
    "departId": "dd211eecf8ce4f8f8435c3b320a5f5bf",
    "pageNo": i,
    "pageSize": 15,
    "roleId": "",
    "serviceStatus": ""
}
        headers = {
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'zh-CN,zh;q=0.9',
          'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiJjZmQ0NjgxMDc0Y2U0YmVkOTA0OTI4ZmI2MDlmYzgyNCIsImFnZW50SWQiOiIxMWE2YTQ3YTRjMmM0NzFiOTMwZTRiY2Y1M2EwZmJmZCIsInNlcnZpY2VFbWFpbCI6ImFsaXlxaWppYW5jamJAMTYzLmNvbSIsInpvbmUiOjAsImlzcyI6ImFsaXlxaWppYW5jamJAMTYzLmNvbSIsImV4cCI6MTcyOTEzMDU2NywidHlwZSI6ImNvbnNvbGUifQ.goK6hWoCtaPnCSrRpbp1RXlp0UfwLkGw5p_AEHF5STE',
          'bno': 'cfd4681074ce4bed904928fb609fc824',
          'cache-control': 'no-cache',
          'content-type': 'application/json;charset=UTF-8',
          'language': 'zh',
          'origin': 'https://console.sobot.com',
          'pragma': 'no-cache',
          'priority': 'u=1, i',
          'referer': 'https://console.sobot.com/',
          'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-site',
          'temp-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiJjZmQ0NjgxMDc0Y2U0YmVkOTA0OTI4ZmI2MDlmYzgyNCIsImFnZW50SWQiOiIxMWE2YTQ3YTRjMmM0NzFiOTMwZTRiY2Y1M2EwZmJmZCIsInNlcnZpY2VFbWFpbCI6ImFsaXlxaWppYW5jamJAMTYzLmNvbSIsInpvbmUiOjAsImlzcyI6ImFsaXlxaWppYW5jamJAMTYzLmNvbSIsImV4cCI6MTcyOTEzMDU2NywidHlwZSI6ImNvbnNvbGUifQ.goK6hWoCtaPnCSrRpbp1RXlp0UfwLkGw5p_AEHF5STE',
          'timezone': '+08:00',
          'timezoneid': 'Asia/Shanghai',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        response = requests.request("POST", url, headers=headers, json=data)
        for item in response.json()["items"]:
            agent_list.append(item["serviceId"])
    return agent_list

agent_list = get_agent_info()
print(f"agentlist 的结果：{agent_list}")
dif_list = ["489e2e49841243a1badc56fa0611a3bb","100f053c13f34e9d9e9e8bfcca3d440a","6f8678597bc84a3fa30aa4d2ea643d8c","d6eedb0fe665474f8d2d56d9630a36d3"]
same_list = []
for item in dif_list:
    if item in agent_list:
        same_list.append(item)

print(f"agentlist 和 dif_list 相同的元素：{same_list}")
