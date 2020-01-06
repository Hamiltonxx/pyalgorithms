N = int(input())
ld,rd = {},{}
ld[1] = 0
rd[0] = 1

for i in range(2,N+1):
    num,lr = map(int,input().split())
    if lr==0:
        x = ld[num]
        rd[x] = i
        ld[i] = x 
        rd[i] = num 
        ld[num] = i  
    else:
        x = rd[num]
        rd[num] = i 
        ld[i] = num 
        rd[i] = x
        ld[x] = i 

M = int(input())
for _ in range(M):
    dn = int(input())
    if dn in rd:
        tmp2 = rd[dn]
        tmp1 = ld[dn]
        rd[tmp1] = tmp2 
        ld[tmp2] = tmp1
        del rd[dn] 

z = 0
while z in rd:
    print(rd[z],end=" ")
    z = rd[z]
