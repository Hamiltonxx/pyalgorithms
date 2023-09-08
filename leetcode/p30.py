from collections import Counter
def findSubstring(s, words):
    m,n = len(words[0]), len(words)
    win = m*n 
    ctr = Counter(words)
    ans = []
    for i in range(len(s)-win+1):
        t = []
        for j in range(i,i+win,m):
            t.append(s[j:j+m])
        if Counter(t) == ctr:
            ans.append(i)
    return ans
