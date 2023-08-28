# # 6  6
# # 1 2 3 4 5 6 

# # 1 2

# # 1 2 3  

# # 1 3 4

# 1 mid

# mid+1 

def f(n, target):
    sm = n*(n+1)//2
    mid = target//2
    if target & 1:
        sm += mid * (n-mid)
    else:
        sm += (mid-1)*(n-mid)

