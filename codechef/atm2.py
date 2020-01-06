T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = ""
    for x in lst:
        if x <= K:
            ans += "1"
            K -= x
        else:
            ans += "0"
    print(ans)