n,m = map(int,input().split())
a = list(map(int, input().split()))

# l = int(input())
# pre = a[l-1]
# ans = len(set(a[l-1:]))
# print(ans)
# for i in range(1,m):
#     l = int(input())
#     if pre in a[l-1:]:
#         print(ans)
#     else:
#         ans -= 1
#         print(ans)
#     pre = a[l-1]

for i in range(m):
    l = int(input())
    ans = len(set(a[l-1:]))
    print(ans)
