import json
import requests




class RobotSession():
    def __init__(self):
        self.session = requests.session()
        url = "http://test.sobot.com/api/get_token?"
        param = {"appid":"1b906d2a500b445c87caf03862f197c1","create_time":"1663583110","sign":"df55f91115902d16a55b7b0193f6ddc6"}
        resp = self.session.get(url = url,params=param)
        rest = json.loads(resp.text)
        self.token = rest.get('item').get('token')

    def get_data(self):
        url = "http://test.sobot.com/api/wb/5/data/robot_session"
        data = {"start_date":"2022-06-01 01","end_date": "2022-09-01 03"}
        json_data = json.dumps(data)
        header = {
            "Content-Type": "application/json",
            "token": self.token}
        resp = self.session.post(url = url, data= json_data, headers = header)
        code = resp.status_code
        rest = json.loads(resp.text)
        print("header>>>",header)
        return code,rest




if __name__ == '__main__':
    r = RobotSession()
    code,rest = r.get_data()
    print("code>>>",code)
    print("rest>>>",rest)

