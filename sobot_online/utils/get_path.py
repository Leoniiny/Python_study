import os,sys,yaml
# 获取当前文件路径
cur_path = os.path.abspath(__file__)
# 获取上一层文件路径
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print("root_path的值为：%s" % root_path)
