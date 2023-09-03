import os
"""
abs():返回数值的绝对值
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False;0、空、False。None为False
compile() 函数将一个字符串编译为字节代码。
    compile(source, filename, mode[, flags[, dont_inherit]])
            mode -- 指定编译代码的种类。可以指定为 exec, eval, single

dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
    带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

"""
print(abs(-3.14))       #3.14
print(all("asdfhjghjfsj"))
print(dir())        #获取当前模块的属性列表

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i,ele in enumerate(seasons):
    print(i,ele)
    i += 1

print(type(enumerate(seasons)))
print(next(enumerate(seasons)))



