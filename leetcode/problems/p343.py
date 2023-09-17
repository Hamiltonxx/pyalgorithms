def integerBreak(n):
    if n <= 3: return n-1
    if n % 3 == 0: return 3**(n//3)
    elif n % 3 == 2: return 3**(n//3) * 2
    else: return 3**(n//3-1) * 2**2

print(integerBreak(2))
print(integerBreak(3))
print(integerBreak(8))
print(integerBreak(16))
print(integerBreak(18))

