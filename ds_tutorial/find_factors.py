def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n%i:
            i +=1
        else:
            n //= i 
            factors.append(i)

    if n > 1:
        factors.append(n)
    return factors 

print(prime_factors(60))

import math
def primeFactors(n):
    factors = []
    while n%2==0:
        factors.append(2)
        n //= 2 
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i 
    if n > 2:
        factors.append(n)
    return factors

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False:
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False 
    return True 

print(primeFactors(60))
print(primeFactors(4))
print(primeFactors(5))
print(primeFactors(6))
