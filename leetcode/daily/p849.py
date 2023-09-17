import math
def maxDistToClosest(seats):
    n = len(seats)
    
    i,j = 0,n-1
    while seats[i]==0:
        i += 1
    while seats[j]==0:
        j -= 1

    mx=0
    cnt=0
    cntstart=False
    for x in seats[i:j+1]:
        if x==0:
            if not cntstart:
                cntstart = True
            cnt += 1
        else:
            if cntstart:
                mx = max(mx, cnt)
                cntstart = False
                cnt = 0
    
    return max(math.ceil(mx/2), i, n-j-1)
