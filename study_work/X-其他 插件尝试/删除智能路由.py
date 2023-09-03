# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import requests,json


def get_sr(bNo=None,temp_id=None):
    url = "http://hk.sobot.com/chat-set/smartRoute/getAllRouteList/4?srStatus=0"
    payload = {}
    headers = {
        'Cookie': '_ga_K3XLQY20V7=GS1.1.1688107979.2.0.1688107979.60.0.0; 030364daa6ee483f9b811d086c993594_u=1b24616c61494c9b90af5d6f64e16159; 913d909e3a194598ba61cf904b5dc12a_u=51cc5535adb744e0a0f1bc54aac57df6; __utma=27390757.1197137664.1688041518.1688365331.1688365331.1; __utmz=27390757.1688365331.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); user_id=1428241750192492545; isFirst=0; nick_name=guyue; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJyb2xlX25hbWUiOiJhZG1pbmlzdHJhdG9yIiwicG9zdF9pZCI6IiIsInVzZXJfaWQiOiIxNDI4MjQxNzUwMTkyNDkyNTQ1Iiwicm9sZV9pZCI6IjEzMjY0NDA0ODgwNTMxNTM3OTQiLCJ1c2VyX25hbWUiOiJndXl1ZUBzb2JvdC5jb20iLCJuaWNrX25hbWUiOiJndXl1ZSIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sInRva2VuX3R5cGUiOiJhY2Nlc3NfdG9rZW4iLCJkZXB0X2lkIjoiIiwiYWNjb3VudCI6Imd1eXVlQHNvYm90LmNvbSIsImV4cCI6MTY4ODY1MjgzMCwibmJmIjoxNjg4NjMxMjMwfQ.f8wBb2UL5RuX3zpNnqlcCk_N9P0FIVHxUaWe_l6oAh3oubMOoHM8dEIytUkxfA5Bpzm8GbQJwsSYJjpdZlnjkw; _gcl_au=1.1.828719602.1688646253; pt_379d489f=uid=M53VTvunTYjaMczvedOpdQ&nid=0&vid=G/SzK20NnCpLalcusQGVZw&vn=3&pvn=1&sact=1688646252587&to_flag=0&pl=2rN7TUmXiLKnhGQMBAbjXg*pt*1688646252587; pt_s_379d489f=vt=1688646252587&cad=; Hm_lvt_8abc47d589af6c5e062a2a368a4baff6=1688049069,1688646253; Hm_lpvt_8abc47d589af6c5e062a2a368a4baff6=1688646253; _ga_T8ZGJQSJJB=GS1.1.1688646252.1.0.1688646254.0.0.0; _ga=GA1.1.1197137664.1688041518; _ga_TKGNGCS09B=GS1.1.1688719467.14.1.1688722300.0.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22903f19d16367426986e13588428aa97c%22%2C%22%24device_id%22%3A%221890713f3cdc9b-06f25ce3f78f52-26031d51-2073600-1890713f3cef4a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_landing_page%22%3A%22http%3A%2F%2Ftest.sobot.com%2Fconsole%2Flogin%22%7D%2C%22first_id%22%3A%221890713f3cdc9b-06f25ce3f78f52-26031d51-2073600-1890713f3cef4a%22%7D',
        'Referer': 'http://hk.sobot.com/imm/online/settings/sessionSetup',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'bNo': bNo,
        'language': 'zh',
        'temp-id': temp_id,
      'timezone': '+08:00',
        'timezoneid': 'Asia/Shanghai'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    srId_list = []
    for i in json.loads(response.text).get("items"):
      srId_list.append(i.get("srId"))
    new_srt = ",".join(list(map(str,srId_list)))
    print(new_srt)
    return srId_list

def delete_sr(bNo=None,temp_id=None):
  srId_list = get_sr()
  for i in srId_list:
    url = "http://hk.sobot.com/chat-set/smartRoute/deleteSmartRoute/4"
    payload = {
      "srId":i
    }
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': '_ga_K3XLQY20V7=GS1.1.1688107979.2.0.1688107979.60.0.0; 030364daa6ee483f9b811d086c993594_u=1b24616c61494c9b90af5d6f64e16159; 913d909e3a194598ba61cf904b5dc12a_u=51cc5535adb744e0a0f1bc54aac57df6; __utma=27390757.1197137664.1688041518.1688365331.1688365331.1; __utmz=27390757.1688365331.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); user_id=1428241750192492545; isFirst=0; nick_name=guyue; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJyb2xlX25hbWUiOiJhZG1pbmlzdHJhdG9yIiwicG9zdF9pZCI6IiIsInVzZXJfaWQiOiIxNDI4MjQxNzUwMTkyNDkyNTQ1Iiwicm9sZV9pZCI6IjEzMjY0NDA0ODgwNTMxNTM3OTQiLCJ1c2VyX25hbWUiOiJndXl1ZUBzb2JvdC5jb20iLCJuaWNrX25hbWUiOiJndXl1ZSIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sInRva2VuX3R5cGUiOiJhY2Nlc3NfdG9rZW4iLCJkZXB0X2lkIjoiIiwiYWNjb3VudCI6Imd1eXVlQHNvYm90LmNvbSIsImV4cCI6MTY4ODY1MjgzMCwibmJmIjoxNjg4NjMxMjMwfQ.f8wBb2UL5RuX3zpNnqlcCk_N9P0FIVHxUaWe_l6oAh3oubMOoHM8dEIytUkxfA5Bpzm8GbQJwsSYJjpdZlnjkw; _gcl_au=1.1.828719602.1688646253; pt_379d489f=uid=M53VTvunTYjaMczvedOpdQ&nid=0&vid=G/SzK20NnCpLalcusQGVZw&vn=3&pvn=1&sact=1688646252587&to_flag=0&pl=2rN7TUmXiLKnhGQMBAbjXg*pt*1688646252587; pt_s_379d489f=vt=1688646252587&cad=; Hm_lvt_8abc47d589af6c5e062a2a368a4baff6=1688049069,1688646253; Hm_lpvt_8abc47d589af6c5e062a2a368a4baff6=1688646253; _ga_T8ZGJQSJJB=GS1.1.1688646252.1.0.1688646254.0.0.0; _ga=GA1.1.1197137664.1688041518; _ga_TKGNGCS09B=GS1.1.1688719467.14.1.1688722300.0.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22903f19d16367426986e13588428aa97c%22%2C%22%24device_id%22%3A%221890713f3cdc9b-06f25ce3f78f52-26031d51-2073600-1890713f3cef4a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_landing_page%22%3A%22http%3A%2F%2Ftest.sobot.com%2Fconsole%2Flogin%22%7D%2C%22first_id%22%3A%221890713f3cdc9b-06f25ce3f78f52-26031d51-2073600-1890713f3cef4a%22%7D',
      'bNo': bNo,
      'language': 'zh',
      'temp-id':temp_id ,
      'timezone': '+08:00',
      'timezoneid': 'Asia/Shanghai'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    g = delete_sr()