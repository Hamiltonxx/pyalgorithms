# s = "abcabcbb"
# s = "bbbb"
s = "pwwkew"
def longest_unrepeated_substring(s):
    n = len(s)
    maxLength = 0
    charSet = set()
    left = 0

    for right in range(n):
        if s[right] not in charSet:
            maxLength = max(maxLength, right-left+1)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
        charSet.add(s[right])

    return maxLength

print(longest_unrepeated_substring(s))