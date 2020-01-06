def counts(lst):
    # if len(lst) < 3:
    #     return 0

    s = sum(lst)

    sa = sb = 0
    ab0 = bc0 = 0
    for i,x in enumerate(lst):
        sa += x 
        if sa*3 == s:
            bc = lst[i+1:]
            for j,y in enumerate(bc):
                if y == 0:
                    ab0 += 1
                else:
                    bc = bc[j:]
                    break
            
            for j,y in enumerate(bc):
                sb += y 
                if sb == sa:
                    c = bc[j+1:]
                    for z in c:
                        if z==0:
                            bc0 += 1
                        else:
                            break
            break
    else:
        return 0
    return (ab0+1)*(bc0+1)


n = int(input())
arr = list(map(int, input().split()))
print(counts(arr))
