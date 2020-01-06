import math
def isPrime(n):
    if n<2: return False 
    if n==2: return True 
    if not n & 1: return False 
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n%x==0:
            return False 
    return True 

l = input()
lst = map(int, input().split())
for x in lst:
    root = math.sqrt(x)
    print(["NO","YES"][int(root)==root and isPrime(int(root))])