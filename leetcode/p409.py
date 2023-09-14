from collections import Counter 
# def longestPalindrome(s):
#     ctr = Counter(s)
#     ans = 0
#     tag = False
#     for x in ctr:
#         if ctr[x] & 1:
#             ans += ctr[x] - 1
#             tag = True
#         else:
#             ans += ctr[x]
#     return ans + int(tag)


def longestPalindrome(s):
    cnt = sum([x//2*2 for x in Counter(s).values()])
    cnt = cnt if cnt==len(s) else cnt+1