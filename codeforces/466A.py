import math
n,m,a,b = map(int, input().split())

resonal = (n // m) * b + (n % m) * a
unresonal1 = n * a 
unresonal2 = math.ceil(n/m) * b 

print(min(resonal,unresonal1,unresonal2))