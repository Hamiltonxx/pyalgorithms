def captureForts(forts):
    mx = j = 0
    for i,x in enumerate(forts):
        if x:
            if x == -forts[j]:
                mx = max(mx, i-j-1)
            j = i
    return mx





