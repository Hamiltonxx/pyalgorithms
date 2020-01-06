N = int(input())
a = list(map(int,input().split()))
avg = sum(a)//N

s=cnt=0
for j,x in enumerate(a):
    s+=x
    if s!=avg*(j+1):
        cnt += 1

print(cnt)
