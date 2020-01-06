
n,m = map(int,input().split())

# if n==1 or m==1:
#     print(1)
if m > n:
    m,n = n,m 
n -= 1
m -= 1

def mul(x,y):
    m = 1
    for i in range(x,y+1):
        m *= i 
    return m

# print(mul(1,n-1)//mul(1,n-m))
# n=100
# m=3
print(mul(n-m+1,n)//mul(1,m))
