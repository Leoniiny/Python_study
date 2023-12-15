import random
list_zz = [
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,
]
list_0 =  []
list_1 =[]
list_2 = []
m = 0
n = 0
o = 0
for j in range(99):
  for i in range(100):
    x =random.choice(list_zz)
    if x == 0:
      list_0.append(x)
    elif x == 1:
      list_1.append(x)
  if len(list_0) > len(list_1):
    m += 1
  if len(list_0) == len(list_1):
    n += 1
  if len(list_0) < len(list_1):
    o += 1
print(f"m  的值为：{m},n  的值为：{n},o  的值为：{o}")