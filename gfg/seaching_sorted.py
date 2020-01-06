import bisect
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    idx = bisect.bisect(arr,K)
    if idx==0 or arr[idx-1]!=K:
        print(-1)
    else:
        print(1)