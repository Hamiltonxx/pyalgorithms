import timeit
# Fibonacci Series
# Fib(n) = Fib(n-1) + Fib(n-2), where Fib(0)=0, Fib(1)=1
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)
# 显然这里会有大量重复计算,时间复杂度(O(2^N))
print(fib(30))
print(timeit.timeit('fib(30)', setup='from __main__ import fib', number=1))

# Top-down (备忘录法)
fibTable = {1:1,2:1}
def fibo(n):
    if n<=2:
        return 1
    if n not in fibTable:
        fibTable[n] = fibo(n-1) + fibo(n-2)
    return fibTable[n]

print(fibo(30))
print(timeit.timeit('fibo(30)', setup='from __main__ import fibo', number=1))

# Bottom-up (表格法)
def fibo2(n):
    fibTable = [0,1]
    for i in range(2,n+1):
        fibTable.append(fibTable[i-1]+fibTable[i-2])
    return fibTable[n]

print(fibo2(30))
print(timeit.timeit('fibo2(30)', setup='from __main__ import fibo2', number=1))

# For all problems, it may not be possible to find both top-down and bottom-up programming solutions.

# Further Improving
# 只需要存两个变量
def fibo3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
print(fibo3(30))
print(timeit.timeit('fibo3(30)', setup='from __main__ import fibo3', number=1))
# 这方法不通用

# 解决DP问题要考虑两点: 1. 能不能递归地定义子问题； 2. 能不能用上table避免重复计算

# Factorial of a Number
# n! = n * (n-1)! where 1!=1, 0!=1
def factorial(n):
    if n==0: return 1
    return n * factorial(n-1)
# There are no repetitive calculations (no overlapping of sub problems),
# the factorial function is not getting any benefits with dynamic programming.

# Longest Common Subsequence
# Given string X of length m, string Y of length n, find the longest common subsequence.
# X="ABCBDAB", Y="BDCABA", LCS(X,Y)={"BCBA","BDAB","BCAB"}
# Recursive solution
# If i==m or j==n: 0
# If X[i]==Y[j]: 1+LCS(i+1,j+1)
# If X[i]!=Y[j]: LCS(i,j+1) or LCS(i+1,j)
def lcs(X, Y):
    if not X or not Y:
        return ""
    if X[0]==Y[0]:
        return X[0] + lcs(X[1:],Y[1:])
    # return max(lcs(X,Y[1:]), lcs(X[1:],Y))
    return [lcs(X,Y[1:]), lcs(X[1:],Y)][len(lcs(X,Y[1:]))<len(lcs(X[1:],Y))]

def lcslen(X, Y):
    if not X or not Y:
        return 0
    if X[0]==Y[0]:
        return 1 + lcslen(X[1:], Y[1:])
    return max(lcslen(X[1:],Y), lcslen(X,Y[1:]))

X="ABCBDAB"
Y="BDCABA"
print(lcs(X,Y))
print(timeit.timeit('lcs("ABCBDAB","BDCABA")', setup='from __main__ import lcs', number=1))
print(lcslen(X,Y))
