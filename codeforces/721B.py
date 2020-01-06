n,k = map(int, input().split())

lst = []
for i in range(n):
    pwd = input()
    lst.append(len(pwd))
lst.sort()

codehorses = len(input())

left = lst.index(codehorses)
right = left+lst.count(codehorses)-1

mi = left+1 + (left//k)*5
ma = right+1 + (right//k)*5

print(mi,ma)

