# n,k = map(int,input().split())
# k -= 1
# l = list(map(int, input().split()))
# if l[k]==0:
#     while k>=0:
#         k -= 1
#         if l[k]>0:
#             break 
# else:
#     while k<n-1:
#         if l[k+1]!=l[k]:
#             break
#         k += 1
# print(k+1)

i = lambda: map(int,input().split())
n,k = i()
l = list(i())
# x = [0<v>=l[k-1] for v in l]
# print(x)
print(sum(0<v>=l[k-1] for v in l))
# print(sum(x))     