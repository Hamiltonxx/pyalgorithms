digit = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
import bisect 

def base10_baseN(x,n):
    ans = ""
    while x:
        ans = digit[x%n] + ans  
        x //= n
    return ans 

def baseN_base10(s,n):
    l = len(s) 
    ans = 0
    for i in range(l):
        idx = bisect.bisect_left(digit,s[i])
        ans += idx*(n**(l-1-i))
    return ans

n = int(input())
a = input()
b = input()
res = baseN_base10(a,n)+baseN_base10(b,n)

print(base10_baseN(res,n)) 
