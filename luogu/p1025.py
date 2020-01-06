# 200球分6个篮，每篮至少一个
# f(n,k) = f(n-1,k-1) + f(n-k,k)

N,K = map(int,input().split())

def f(n,k):
    if n<k: return 0
    if k==1: return 1
    if n==k: return 1
    return f(n-1,k-1)+f(n-k,k)

print(f(N,K))
