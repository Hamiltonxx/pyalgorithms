# import bisect
def min_k_avoid(n,k):
    if k >(n-1)+n or k<3:
        return n*(n+1)//2

    mid = k//2
    if k & 1:
        # mn = min(mid, n-mid)
        return mid*(n-mid) + n*(n+1)//2
    else:
        # mn = min(mid-1,n-mid)
        return n*(n+1)//2 + (mid-1)*(n-mid)