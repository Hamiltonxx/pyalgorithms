# def divisors(n):
#     divs = [1,n]
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             divs.extend([i,n//i])
#     return list(set(divs))

# 返回所有因子的集合
def divisors(n):
    divs = set([1,n])
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divs |= {i,n//i}
    return divs

# print(divisors(18))
# print(divisors(36))
# print(divisors(100))

# n的所有质因子
def primeFactors(n):
    factors = []
    while n%2==0:
        factors.append(2)
        n //= 2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            factors.append(i)
            n //= i 
    if n>1:
        factors.append(n)
    return factors

def maxPrimeFactor(n):
    mx = -1
    while n%2==0:
        mx = 2
        n //= 2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            mx = i
            n //= i 
    if n>2:
        mx = n 
    return mx

def isPrime(n):
    if n<2: return False 
    if n==2: return True 
    if n%2==0: return False 
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False 
    return True 