# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：

import requests, json


def query(tempid):
	# 需要修改 url，tempid，kbid
	url = "https://hk.sobot.com/kb-inner-service/innerDoc/list"
	payload = {
		"pageNo": 1,
		"pageSize": 15,
		"createId": None,
		"updateId": None,
		"kbType": None,
		"ifReaded": None,
		"isSub": 0,
		"orderType": 2,
		"createStartDate": None,
		"createEndDate": None,
		"updateStartDate": None,
		"updateEndDate": None,
		"effectStartDate": None,
		"effectEndDate": None,
		"invalidStartDate": None,
		"invalidEndDate": None,
		"kbId": "5",
		"kbStatus": None,
		"keyFlag": 1,
		"keyWords": None,
		"questionTypeId": "-1",
		"isManageOrQuery": 1
	}
	headers = {
		'Content-Type': 'application/json;charset=UTF-8',
		'temp-id': tempid
	}
	response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
	rest = json.loads(response.text)
	print(f"rest 的值为{rest}")
	temp_li = rest.get("items")
	page_num = rest.get("pageCount")
	temp_info_list = []
	if temp_li:
		for doc_info in temp_li:
			kbDocId = doc_info.get("kbDocId")
			temp_info_list.append(kbDocId)
	return temp_info_list,page_num


def delete_doc(tempid):
	temp_info_list,page_num = query(tempid)
	print(f"temp_info_list   的值为{temp_info_list}")
	print(f"page_num   的值为{page_num}")
	for i in range(page_num):
		print(f'temp_info_list 的值为{temp_info_list}')
		if temp_info_list:
			url = "https://hk.sobot.com/kb-inner-service/innerDoc/deleteList"
			payload = {'kbDocIdList':temp_info_list}
			headers = {
				'Content-Type': 'application/json;charset=UTF-8',
				'temp-id': tempid}
			response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
			print(response.text)
		else:
			print(f'temp_info_list 的值为{temp_info_list}')


if __name__ == '__main__':
	pass
	tempid  = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJseXBAaGsuY29tIiwiZXhwIjoxNjg2OTY5MTgyfQ.Wib9bRE9ZgGDEMF3uyHeWXTgjvqevE7srIdbh5fSQwA'
	# QE = query()
	delete_doc(tempid)
