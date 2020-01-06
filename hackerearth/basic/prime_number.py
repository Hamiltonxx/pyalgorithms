def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if not n & 1: return False 
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False 
    return True 

N = int(input())
# for i in range(1,N+1):
#     if isPrime(i):
#         print(i,end=" ")
primes = filter(isPrime,range(1,N+1))
print(" ".join(map(str,primes)))