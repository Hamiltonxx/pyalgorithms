def isSub(s, t):
    m, n = len(s), len(t)
    i = j = 0
    while i<m and j<n:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == m
        