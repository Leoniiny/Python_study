import json

import requests

url = "https://test-branche1.sobot.com/text/chat-set/reception/getSchemeList?status=1&name=&page=1&pageSize=999999"

payload = {}
headers = {
  'authority': 'test-branche1.sobot.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'bno': '443af7afa23f4c87a8900f178137d09c',
  'cache-control': 'no-cache',
  'language': 'zh',
  'origin': 'https://testconsole.sobot.com',
  'pragma': 'no-cache',
  'referer': 'https://testconsole.sobot.com/',
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'temp-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI0NDNhZjdhZmEyM2Y0Yzg3YTg5MDBmMTc4MTM3ZDA5YyIsImFnZW50SWQiOiI5YmRlNTI4N2I3OWI0ODA3YjcxNzkwZWE5OGRiNWQzZiIsInNlcnZpY2VFbWFpbCI6ImNzeGIwMkBxcS5jb20iLCJ6b25lIjowLCJpc3MiOiJjc3hiMDJAcXEuY29tIiwiZXhwIjoxNzAyMTAwMjQ3LCJ0eXBlIjoiY29uc29sZSJ9.r_k62QSSMi8Y67KDXXF_QovEO_zZxhs7Qvb1XtWgqnk',
  'timezone': '+08:00',
  'timezoneid': 'Asia/Shanghai',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

li01 = json.loads(response.text).get("items")

id_list = [id_info.get("id") for id_info in li01]
print(id_list)


for i in range(len(id_list)-1):
    id_info1 = id_list[i]
    url = "https://test-branche1.sobot.com/text/chat-set/reception/updateScheme"

    payload = f'id={id_info1}&status=0'
    headers = {
      'authority': 'test-branche1.sobot.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'zh-CN,zh;q=0.9',
      'bno': '443af7afa23f4c87a8900f178137d09c',
      'cache-control': 'no-cache',
      'content-type': 'application/x-www-form-urlencoded',
      'language': 'zh',
      'origin': 'https://testconsole.sobot.com',
      'pragma': 'no-cache',
      'referer': 'https://testconsole.sobot.com/',
      'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'temp-id': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI0NDNhZjdhZmEyM2Y0Yzg3YTg5MDBmMTc4MTM3ZDA5YyIsImFnZW50SWQiOiI5YmRlNTI4N2I3OWI0ODA3YjcxNzkwZWE5OGRiNWQzZiIsInNlcnZpY2VFbWFpbCI6ImNzeGIwMkBxcS5jb20iLCJ6b25lIjowLCJpc3MiOiJjc3hiMDJAcXEuY29tIiwiZXhwIjoxNzAyMTAwMjQ3LCJ0eXBlIjoiY29uc29sZSJ9.r_k62QSSMi8Y67KDXXF_QovEO_zZxhs7Qvb1XtWgqnk',
      'timezone': '+08:00',
      'timezoneid': 'Asia/Shanghai',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

