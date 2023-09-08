# 字母异位词
from collections import Counter 
Counter("silent") == Counter("listen")

# 列表推导式的for,if
even = [x for x in [1,2,3,4] if x%2==0]

# 列表中最长的字符串
words = ['This', 'is', 'a', 'list', 'of', 'words']
mx = max(words, key=len)

# 检查数据类型
print(isinstance([3,4,1997], list))
print(type("hello")==str)

# 既打印信息，又保存文件
# print("Hello World!", file=open('file.txt','w'))

# 合并 list, set, dict
l1,l2 = [1,2,3],[3,4,5]
# l1.extend(l2);print(l1)
print(l1 + l2)
s1,s2 = {1,2,3},{3,4,5}
# print(s1.union(s2))
print(s1 | s2)
d1,d2 = {'a':0,'b':1},{'b':1,'c':2}
# d1.update(d2);print(d1)
print(d1 | d2)
print({**d1, **d2})

# 列表中出现次数最多的元素
nums = [9, 4, 5, 4, 4, 5, 9, 5, 4]
most_frequent_element = max(nums, key=nums.count)
print(most_frequent_element)

# 二/八/十六进制转十进制
print(int('1101',2));print(int('30',8));print(int('da9',16))
# 十进制转二/八/十六进制
print(bin(344));print(oct(344));print(hex(344))

# 两个列表转字典
keys,values = ['a','b','c'],[0,1,2]
d = dict(zip(keys,values))

# 求商和余数
quotient,remainder = divmod(4,5)

# 获取小写字母表
import string 
print(string.ascii_lowercase)

# 将字符串中的数字移除
import re; print(re.sub(r'\d+','','H3ll0 W0rld!'))
print(''.join(filter(lambda x:x.isalpha(), 'H3ll0 W0rld!')))

# 矩阵变换
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrixT = list(zip(*matrix))
print(matrixT)

# 解包
a, *b, c = [1,2,3,4,5]
print(a);print(b);print(c)