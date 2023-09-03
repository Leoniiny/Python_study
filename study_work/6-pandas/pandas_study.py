import pandas as pd
'''
# 1、初识pandas  ---  读取文件
# 创建pandas  read方法的示例对象   默认值参数时取的是当前脚本所在文件夹下的。r = raw 原生
# 获取csv 文件内容
df = pd.read_csv(r"..\Data_base\nba.csv")
# to_string() 将内容转换成字符串
print(df.to_string())
print(df)


# 2、初识pandas  ---  存储文件
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
age = [90, 40, 80, 98]
dict = {'name': nme, 'site': st, 'age': age}
# 创建DataFrame对象，默认值参数 是当前脚本所在文件夹下的文件
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv(r'../Data_base/site.csv')
'''
# 3、Pandas 数据结构 - Series -- 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
# pandas.Series( data, index, dtype, name, copy)
        # data：一组数据(ndarray 类型)。
        # index：数据索引标签，如果不指定，默认从 0 开始。
        # dtype：数据类型，默认会自己判断。
        # name：设置名称。
        # copy：拷贝数据，默认为 False。

l_a = [1,2,3]
myvar = pd.Series(l_a)
print(myvar)