import math
n = int(input())
lst = map(int, input().split())

a = 0

for x in lst:
    a = math.gcd(a,x)

print(a*n)
