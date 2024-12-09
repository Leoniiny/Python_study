# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import requests, re, json
from urllib.parse import urlencode
from sobot_online.Bs_layer.bs_login import Login
from faker import Faker


class RulesEngine(Login):
    def __init__(self):
        super().__init__()
        pass

    def get_canvas_list(self, status=0, name='', pageSize=15, pageNo=1):
        url = self.host + "/logi-canvas/canvas/getCanvasList"
        json_data = {
            "status": status,
            "name": name,
            "pageSize": pageSize,
            "pageNo": pageNo
        }
        headers = {
            'bno': self.bno,
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid
        }
        response = self.session.post(url, headers=headers, json=json_data)
        return response.text

    def update_canvas(self, canvas_id='1767086735490211840', status=2):
        url = self.host + "/logi-canvas/canvas/updateCanvas"
        json_data = {
            "id": canvas_id,
            "status": status
        }
        headers = {
            'bno': self.bno,
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid
        }
        response = self.session.post( url, headers=headers, json=json_data)
        return response.text

    # 删除画布
    def delete_canvas(self, canvas_id='1767086735490211840'):
        url = self.host + "/logi-canvas/canvas/delCanvas"
        json_data = {
            "id": canvas_id
        }
        headers = {
            'bno': self.bno,
            'content-type': 'application/json;charset=UTF-8',
            'temp-id': self.tempid
        }
        response = self.session.post( url, headers=headers, json=json_data)
        print(f"删除画布结果：{response.text}")
        return response.text

if __name__ == '__main__':
    obj = RulesEngine()
    rest = obj.get_canvas_list(status=0)
    if json.loads(rest).get('items'):
        canvas_id_list = [canvas_id_info.get('id') for canvas_id_info in json.loads(rest).get('items')]
        for canvas_id in canvas_id_list:
            obj.update_canvas(canvas_id=canvas_id)
            # obj.delete_canvas(canvas_id=canvas_id)
