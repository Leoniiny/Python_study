# @Time : 2023/3/20 0020 13:51
# @Author : 雷洋平
# @File : 10-yamlfile.py
# @Software: PyCharm
# @Function:yaml 文件学习

import yaml
import os


class YamlFile:
    # 获取当前脚本所在文件夹路径
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(f"current_path 为{current_path}")
    # 获取yaml文件路径
    yaml_file_path = os.path.join(current_path, "temp_data.yml")

    def __init__(self):
        pass

    # 获取yaml文件内容
    def get_yml_content(self):
        with open(YamlFile.yaml_file_path, mode='r', encoding='utf-8') as fp:
            file_data = yaml.load(fp, Loader=yaml.FullLoader)
            return file_data

    # 更新yaml文件中的信息
    def update_content(self, key, data):
        with open(YamlFile.yaml_file_path, encoding='utf-8') as fp:
            dict_content = yaml.load(fp, Loader=yaml.FullLoader)
            try:
                dict_content[key] = data
            except:
                if not dict_content:
                    dict_content = {}
                dict_content.update({key: data})
        with open(YamlFile.yaml_file_path, 'w', encoding='utf-8') as fp:
            yaml.dump(dict_content, fp, allow_unicode=True)


if __name__ == '__main__':
    yf = YamlFile()
    # file_data = yf.get_yml_content()
    # yf.update_content("test", {"test1":"测试01","test2":"测试02"})
    file_data = yf.get_yml_content()["agent_dic"][0]
    id = list(dict(yf.get_yml_content()["agent_dic"][0]).values())[0]
    print(f"file_data 的值为{id}")
