# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：画布
import requests,json


class Canvas():
    def __init__(self):
        self.session = requests.session()

    def getcanvaslist(self,status=0,name="",tempid=None,pageNo=1,host = "https://test-branche1.sobot.com/text"):
        '''

        :param status: 0：启用；2：停用
        :param name:
        :param tempid:
        :param pageNo:
        :param host:
        :return:
        '''
        url =host + "/logi-canvas/canvas/getCanvasList"
        data = {
            "status":status,
            "name":name,
            "pageSize":15,
            "pageNo":pageNo
        }
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': tempid}
        response = self.session.post(url, headers=headers, data=json.dumps(data))
        if response.text:
            print(f"response.text 的值为：{response.text}")
            canvaslist = [canvasinfo.get("id") for canvasinfo in json.loads(response.text).get("items")]
            print(f"canvaslist 的值为：{canvaslist}")
            return canvaslist

    def updateCanvas(self,canvasid=None,status=2,tempid=None,host = "https://test-branche1.sobot.com/text"):
        url = host + "/logi-canvas/canvas/updateCanvas"
        data = {
            "id":canvasid,
            "status":status
        }
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': tempid
        }
        response = self.session.post( url, headers=headers, data=json.dumps(data))
        rest = json.loads(response.text)
        print(rest)
        if rest["item"]:
            rest_id = rest.get("item").get("id")
            print(f"rest_id 的值为:{rest_id}")
            return rest_id


if __name__ == '__main__':
    pass
    # host = "https://hk.sobot.com"

    tempid ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI0NDNhZjdhZmEyM2Y0Yzg3YTg5MDBmMTc4MTM3ZDA5YyIsImFnZW50SWQiOiI5YmRlNTI4N2I3OWI0ODA3YjcxNzkwZWE5OGRiNWQzZiIsInNlcnZpY2VFbWFpbCI6ImNzeGIwMkBxcS5jb20iLCJ6b25lIjowLCJpc3MiOiJjc3hiMDJAcXEuY29tIiwiZXhwIjoxNzAwMDE1MTIxLCJ0eXBlIjoiY29uc29sZSJ9.D8CzfG4d9O3n2tWF1glACOJ_mpzsAqPTOjVm9fuTBkg"


    obj = Canvas()
    canvaslist = obj.getcanvaslist(tempid=tempid,pageNo=1)

    if canvaslist:
        for canvasid in canvaslist:
            obj.updateCanvas(canvasid=canvasid,tempid=tempid)
    else:
        print(f"canvaslist 为空")