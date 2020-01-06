n = int(input())
lst = list(map(int, input().split()))
c = t = 0

s = sum(lst)
if s%3==0:
    sone = s // 3
    stwo = s - sone
    s = 0
    for x in lst[:n-1]:
        s += x 
        if s == stwo:
            c += t
        if s == sone:
            t += 1
print(c) 