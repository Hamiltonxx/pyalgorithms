n,k = map(int, input().split())
a = list(map(int, input().split()))

diff = sorted([(y-x) for x,y in zip(a,a[1:])])
print(sum(diff[:n-k]))