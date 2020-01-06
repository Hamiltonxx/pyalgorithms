from itertools import combinations
import bisect
line = input()
l = len(line)
if l & 1:
    ans = "4"*(l//2+1)+"7"*(l//2+1)
else:
    if int(line)==10**9:
        exit(print("4444477777"))
    half = l//2
    if line > "7"*half+"4"*half:
        ans = "4"*(half+1)+"7"*(half+1)
    # elif line <= "4"*half+"7"*half:
    #     ans = "4"*half+"7"*half
    else:
        lst = []
        if l==2:
            lst = ["47","74"]
        elif l==4:
            lst = ["4477","4747","4774","7447","7474","7744"]
        elif l==6:
            num = list("777777")
            for i,j,k in combinations(range(6),3):
                num[i]=num[j]=num[k]="4"
                lst.append("".join(num))
                num = list("777777")
        elif l==8:
            num = list("77777777")
            for i,j,k,m in combinations(range(8),4):
                num[i]=num[j]=num[k]=num[m]="4"
                lst.append("".join(num))
                num = list("77777777")
        idx = bisect.bisect_left(lst,line)
        ans = lst[idx]
print(ans)
