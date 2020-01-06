import math
def primeFactors(n):
    factors = []
    while n%2==0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i==0:
            factors.append(i)
            n //= i 
    if n>2:
        factors.append(n)
    return factors

# l = int(input())
# lst = map(int,input().split())
# for x in lst:
#     # divisors = set(primeFactors(x))
#     factors = primeFactors(x)
#     # if (len(divisors)==1 and x not in divisors) or (len(divisors)==2 and x in divisors):
#     #     print("YES")
#     # else:
#     #     print("NO")
#     if (len(factors)==1 and x not in factors) or (len(factors)==2 )


