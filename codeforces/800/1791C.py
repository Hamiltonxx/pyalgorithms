# [*open(0)] put every line of stdin into a list.
for h in [*open("1791C.txt")][2::2]:
    i,j = 0,len(h)-2
    while i<j and h[i]!=h[j]:
        i += 1
        j -= 1
    print(j-i+1)


