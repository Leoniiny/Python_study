# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.common.utils import *
import pandas,sys
import yaml


# 读取yaml文件的方法
def load_yaml_file(filepath):
    with open(Projection_PATH + filepath, mode='r', encoding='UTF-8') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_content


def write_yaml(filepath, content):
    with open(Projection_PATH + filepath, mode='w', encoding='UTF-8') as f:
        yaml.dump(content, f, Dumper=yaml.Dumper)


# 更新配置文件
def renewal_yaml(file_path, key, value):
    with open(Projection_PATH + file_path, encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        try:
            content[key] = value
        except:
            if not content:
                content = {}
            content.update({key: value})
    with open(Projection_PATH + file_path, mode="w", encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)


# 读取excel文件的方法
def read_excel(filepath, sheet_name):
    # keep_default_na=False 参数的意思是读到空单元格时，他的值是空字符串
    res = pandas.read_excel(Projection_PATH + filepath, sheet_name=sheet_name, keep_default_na=False, engine='openpyxl')
    # 将res中的数据转换成pytest参数化所需要的列表数据
    # print(res.shape)
    lines_count = res.shape[0]  # 获取总行数
    # print(res.shape[1])
    col_count = res.columns.size  # 获取总列数
    # print(lines_count)
    # print(col_count)
    # print(res)
    data = []  # 定义列表，用来存储多行数据
    for i in range(lines_count):  # 遍历行
        line_data = []  # 定义一个列表，用来存储当前行所有列的数据
        for j in range(col_count):  # 遍历列
            cell_data = res.iloc[i, j]  # 传行和列得到当前单元格数据
            line_data.append(cell_data)
        data.append(line_data)
    return data


# 解决储存临时数据没地方储存的问题：如tempid等
def update_yaml_content(file_path, key, value):
    with open(Projection_PATH + file_path, encoding='utf-8') as fp:
        dict_content = yaml.load(fp, Loader=yaml.FullLoader)
        try:
            dict_content[key] = value
        except:
            if not dict_content:
                dict_content = {}
            dict_content.update({key: value})
    with open(Projection_PATH + file_path, 'w', encoding='utf-8') as fp:
        yaml.dump(dict_content, fp, allow_unicode=True)  # allow_unicode=True，解决储存时，Unicode编码问题


if __name__ == '__main__':
    pass
    # agents = list(load_yaml_file(filepath=r"\Online\config\temp_data.yml")["agent_dic"][0].values())[0]
    # print(agents)
    key = "config"
    value = "AL"
    file_path = r'''/config_file/operation_config.yml'''
    renewal_yaml(file_path, key, value)
