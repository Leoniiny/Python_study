import re
import pandas
'''
1.通过span()提取匹配到的字符下标
2.通过group()提取匹配到的内容
'''
str = "1111python12313python243python8888"
# 一、匹配的基本方法
# # 1、match：从字符串的起始位置匹配，匹配成功则返回的是一个匹配对象，否则返回None。
# match_obja = re.match("python",str)
# print(match_obja)
# match_objb = re.match("1",str)
# print(match_objb)
# match_objb1_rest = match_objb.group()   #返回内容
# print(match_objb1_rest)
# match_objb2_rest = match_objb.span()    #返回下标
# print(match_objb2_rest)


# 2、search：扫描整个字符串,匹配成功则返回的是一个匹配对象,没有则返回None
# # 获取的是一个正则对象
# search_obj1 = re.search("as",str)
# print(search_obj1,type(search_obj1),sep="   ")
# search_obj2 = re.search("python",str)
# print(search_obj2,type(search_obj2),sep="   ")
# search_obj2_r1 = search_obj2.span()
# print(search_obj2_r1)
# search_obj2_r2 = search_obj2.group()
# print(search_obj2_r2)

# 3、findall：在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# findall_list1 = re.findall("pythoX", str)
# print("findall_obj1>>", findall_list1)  # 返回空列表
# findall_list2 = re.findall("python", str)
# print("findall_obj2>>", findall_list2)

# 二、元字符匹配规则
'''
1、单字符匹配
.：匹配任一字符
[]：匹配[]中列举的字符
\d：匹配数字，0-9
\D：匹配非数字
\s：匹配空白，比如：空格，tab
\w：匹配单词字符，a-z，A-Z，0-9，_

2、数量元字符
*：匹配前一个字符出现0次或者无数次，即可有可无
+：匹配前一个字符出现1次或者无数次，即至少一次
?：匹配前一个字符出现1次或者0次，
{m}：匹配前一个字符出现m次
{m,}：匹配前一个字符至少出现m次
{m,n}：匹配前一个字符出现从m次到n次

3、边界元字符
^：以什么开头
$：以什么结尾

4、分组匹配
|：匹配左右任一一个表达式
(ab)：将括号中的字符看成一个整体进行匹配
'''
# 例子：
s = "1311234sd567asdfgh1"
match_obj = re.match(r"^1[0-9a-zA-Z]{9}",s)   #前面的字符至少出现10次
print(match_obj)
match_rest = match_obj.group()
print(match_rest)











