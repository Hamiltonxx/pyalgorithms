# def longestPalindrome(s):
#     N = len(s)
#     for n in range(N,0,-1):
#         start = 0
#         while start+n<=N:
#             t = s[start:start+n]
#             if t == t[::-1]:
#                 return n
#             start += 1

def longestPalindrome(s):
    n = len(s)
    def expand(l, r):
        while l>=0 and r<n and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    mx = ''
    for i in range(n):
        p1 = expand(i, i) # odd length palindrome
        p2 = expand(i, i+1) # even length palindrome
        mx = max([mx, p1, p2], key=len)

    return mx