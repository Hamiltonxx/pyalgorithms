# 1 2 3 4 5 (4) 3->6
# 1 2 3 4 5 6 7 8 (8)  (10)   
def kavoiding(n, k):
    if k>n+(n-1) or k<1+2:
        return n*(n+1)//2
    
    small = range(1, k//2+1)
    big = range(k, k+n-k//2)

    return sum(small) + sum(big)
