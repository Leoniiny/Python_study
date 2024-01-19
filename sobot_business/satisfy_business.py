# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import json

import requests


# aaa = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI0NDNhZjdhZmEyM2Y0Yzg3YTg5MDBmMTc4MTM3ZDA5YyIsImFnZW50SWQiOiJjNjE0NTZmNzVjYmY0M2ZkYjA5ODBjMzdhNGYyYjQ5YyIsInNlcnZpY2VFbWFpbCI6ImNzeGIwMUBxcS5jb20iLCJ6b25lIjowLCJpc3MiOiJjc3hiMDFAcXEuY29tIiwiZXhwIjoxNzA1NTU3MjEwLCJ0eXBlIjoiY29uc29sZSJ9.wYJQq7t8R_SliEmmsarYfOPcfgCqlL9C1ekTIky63wY"



def satisfy_sction(tempid=None):
    url = "https://test-branche1.sobot.com/text/chat-satisfaction/saticfaction/getLabels"
    payload = {}
    headers = {
      'temp-id': tempid}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    # label_list = [label_id_info.get("id") for label_id_info in json.loads(response.text).get("items")]
    # print(label_list)


    # for label_num in range(len(label_list)):
    #     url = "https://test-branche1.sobot.com/text/chat-satisfaction/saticfaction/delLabel"
    #     payload = f'labelId={label_list[label_num]}'
    #     headers = {
    #       'content-type': 'application/x-www-form-urlencoded',
    #       'temp-id': aaa
    #     }
    #     response = requests.request("POST", url, headers=headers, data=payload)
    #     print(response.text)

if __name__ == '__main__':
    tempid = input("请输入tempid：")
    satisfy_sction(tempid=tempid)
