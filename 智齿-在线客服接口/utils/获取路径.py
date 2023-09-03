import os,sys,yaml
# 获取当前文件路径
cur_path = os.path.abspath(__file__)
# 获取上一层文件路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"公司ID.yml")
    print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"公司ID.yml"))
    with open(yaml_path,"r",encoding="utf8") as f:
        content = f.read()
    d = yaml.dump(content)
    print(content,type(content))
    print(d)
