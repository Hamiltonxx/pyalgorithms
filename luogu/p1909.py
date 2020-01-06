import math
n = int(input())
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())

mn = min(math.ceil(n/a1)*b1, math.ceil(n/a2)*b2, math.ceil(n/a3)*b3)

print(mn)