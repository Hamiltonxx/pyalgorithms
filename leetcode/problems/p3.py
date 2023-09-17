# s = "abcabcbb"
# s = "bbbb"
# s = "pwwkew"
s = "tmmzuxt"
def longest_unrepeated_substring(s):
    # n = len(s)
    # maxLength = 0
    # charSet = set()
    # left = 0

    # for right in range(n):
    #     if s[right] not in charSet:
    #         maxLength = max(maxLength, right-left+1)
    #     else:
    #         while s[right] in charSet:
    #             charSet.remove(s[left])
    #             left += 1
    #     charSet.add(s[right])

    # return maxLength

    seen = {}
    l = mx = 0
    n = len(s)
    for r,x in enumerate(s):
        if x in seen and seen[x] >= l:
            l = seen[x] + 1
        else:
            mx = max(mx, r-l+1)
        seen[x] = r
    return mx

print(longest_unrepeated_substring(s))