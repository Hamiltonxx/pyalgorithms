from collections import defaultdict
from functools import lru_cache
def lps(s):
    d = defaultdict(int)
    @lru_cache(None)
    def f(s):
        if s not in d:
            for c in set(s):
                i, j = s.find(c), s.rfind(c)
                d[s] = max(d[s], 1 if i==j else f(s[i+1:j])+2)
        return d[s]
    return f(s)