# 4, 7, 13, 15, 19
# 2, 4, 5, 6, 8, 9, 11, 14, 16, 18, 19, 21

def findContentChildren(g, s):
    g.sort()
    s.sort()
    print(g)
    i = j = 0
    while i<len(g) and j<len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1
    return i
    
g = [10,9,8,7]
s = [5,6,7,8]
print(findContentChildren(g,s))