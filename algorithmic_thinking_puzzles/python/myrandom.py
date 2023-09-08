import random 

print(random.getrandbits(8)) # 8 bits sized integer
print(random.randrange(5,10)) # a number between [5,10)
print(random.randint(5,10)) # a number between [both included]
r = random.random()
print(r) # a floating number between 0 and 1
# print(type(round(r,2)))
print(round(r,2)) # 保留两位小数
print(random.uniform(10,20)) # a floating number between []
lst = ['apple','banana','cherry']
print(random.choice(lst))
print(random.choice('WELCOME'))
print(random.sample(lst, k=2)) # k: the size of the returned list
random.shuffle(lst)
print(lst)

# 生成不重复随机数列
randomlist = random.sample(range(10,30), 5)
print(randomlist)
# 生成允许重复的随机数列
randomlist = [random.randrange(10) for _ in range(8)]
print(randomlist)
import numpy as np
randomlist = list(np.random.choice(10,8,replace=True))
print(randomlist)