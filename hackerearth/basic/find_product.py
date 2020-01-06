from functools import reduce

input()
a = map(int,input().split())

mul = reduce(lambda x,y:x*y, a)

print(mul % (10**9+7))