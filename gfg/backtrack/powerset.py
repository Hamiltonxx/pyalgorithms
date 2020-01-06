# Time Complexity O(n2^n)
# def printPowerSet(s):
#     l = len(s)
#     pow2l = 1 << l  # 2**l

#     for i in range(pow2l):
#         for j in range(l):
#             if i & (1<<j):
#                 print(s[j], end="")
#         print("")

# # test code
# s = "abc"
# printPowerSet(s)

def powersetLoop(seq):
    n = len(seq)
    for i in range(1<<n): # 2**n
        print([seq[j] for j in n if (i & 1<<j)])

def powersetBT(seq):
    if len(seq) <= 0:
        yield []
    else:
        for item in powersetBT(seq[1:]):
            yield item 
            yield [seq[0]] + item 

from itertools import chain,combinations
def powersetLib(seq):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    # s = list(iterable)
    return chain.from_iterable(combinations(seq, r) for r in range(len(seq)+1))

print(list(powersetBT("ABC")))
print(list(powersetLib("ABC")))
