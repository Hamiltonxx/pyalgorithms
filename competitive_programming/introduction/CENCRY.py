from sys import stdin
from collections import defaultdict

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

# n = int(input())
n = int(stdin.readline())
for _ in range(n):
    # s = input()
    s = stdin.readline().strip()
    d = defaultdict(int)
    res = []
    for x in s:
        if x in vowels:
            pos = vowels.index(x) + d[x] * 5
            rep = consonants[pos % 21]
        else:
            pos = consonants.index(x) + d[x] * 21
            rep = vowels[pos % 5]
        d[x] += 1
        res.append(rep)
    print(''.join(res))
        