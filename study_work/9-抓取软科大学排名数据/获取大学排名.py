# @Time : 2023/3/2 0002 15:21
# @Author : 雷洋平
# @File : 获取大学排名.py
# @Software: PyCharm
# @Function:
import requests, json, csv


class GetUniversityRank():
    def __init__(self):
        pass

    #   声明类方法
    @classmethod
    def get_university_rank(cls, lemmaId=50359848, nodeId="d73dbd027883f2d1de20c0e6", pn=1, rn=100):
        url = f"https://baike.baidu.com/starmap/api/getlemmalist?lemmaId={lemmaId}&nodeId={nodeId}&pn={pn}&rn={rn}"
        session = requests.Session()
        r = session.get(url=url)
        rest = json.loads(r.text)
        # 获取大学排名
        university_list = rest.get("data").get("list")
        # print(university_list)
        return university_list

    @classmethod
    def write_csv(cls):
        # 类方法调用
        university_list = cls.get_university_rank()
        headers = ["大学名称", "大学简介"]
        # 创建一个二维列表
        matrix_list = []
        for university_info_dic in university_list:
            temp_list = []
            temp_list.append(university_info_dic.get("lemmaTitle"))
            temp_list.append(university_info_dic.get("summary"))
            matrix_list.append(temp_list)
        with open("./大学排名.csv", mode="w", encoding="utf-8", newline="") as fp:
            #   创建写的实例化对象
            writer = csv.writer(fp)
            #     设置第一行标题头
            writer.writerow(headers)
            #   写入数据
            writer.writerows(matrix_list)
        return matrix_list


if __name__ == '__main__':
    GUR = GetUniversityRank()
    matrix_list = GUR.write_csv()
    print(matrix_list)
