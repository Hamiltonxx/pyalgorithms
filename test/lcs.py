from collections import defaultdict
import bisect
def lcs(word1, word2):
    if len(word1) > len(word2): word1, word2 = word2, word1
    d, a = defaultdict(list), []
    for i,x in enumerate(word2):
        d[x].append(i)
    for x in word1:
        if x in d:
            for i in reversed(d[x]):
                idx = bisect.bisect_left(a, i)
                if idx == len(a):
                    a.append(i)
                else:
                    a[idx] = i
    return len(a)

# word1, word2 = "sea", "eat"
word1, word2 = "leetcode", "etce"
print(lcs(word1, word2))