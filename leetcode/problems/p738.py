def monotone(n):
    s = str(n)
    l = len(s)
    first = s[0]
    if s <= first * l:
        ans = str(int(first)-1) + '9'*(l-1)
    else:
        ans = s[0]
        for i in range(1,l):
            if s[i] < s[i-1]:
                ans += ans[-1]
            else:
                ans += s[i]
    return int(ans)
        