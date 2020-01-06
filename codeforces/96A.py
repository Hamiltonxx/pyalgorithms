line = input()
cnt = 1
for i in range(1,len(line)):
    if line[i] != line[i-1]:
        cnt = 1
    else:
        cnt += 1
        if cnt == 7:
            break 
if cnt==7:
    print("YES")
else:
    print("NO")
