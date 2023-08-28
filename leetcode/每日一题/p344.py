def reverseString(s):
    l = len(s)
    n = l//2
    for i in range(n):
        s[i], s[l-1-i] = s[l-1-i], s[i]
    return s

print(reverseString(list('hello')))