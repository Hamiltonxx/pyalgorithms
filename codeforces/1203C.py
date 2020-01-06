from math import gcd  
from functools import reduce

# find divisors
def divisors(n):
    divs = set([1,n])
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divs |= {i,n//i}
    return divs

n = int(input())
# a = [*map(int,input().split())]
# g = reduce(gcd,a)
g = reduce(gcd,map(int,input().split()))

print(len(divisors(g)))