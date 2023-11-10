# check odd number 
print(7 & 1)

# 7: 0111, 4: 0100
print(7 & 4)
print(7 | 4)
print(7 ^ 4)
print(~7)
print(~9) # 最高位是1，表示负数.

print(5 << 1)
print(5 >> 1)

num = 1024
print(bin(num))
print(bin(num)[2:].zfill(32))
print(bin(num<<1)[2:].zfill(32))
print(bin(num<<2)[2:].zfill(32))

# set a bit at postion pos
print(4 | (1<<1))
# unset/clear a bit at position pos
print(7 & (~(1<<1)))
# toggling a bit at position pos
print(7 ^ (1<<1))
# check a bit at position pos
print(5 & (1<<2))

# multiply/divide by 2
print(5 << 1)
print(5 >> 1)

# compute xor from 1 to n, 1^2^3...^n
# Find the remainder of n by moduling it with 4. 0=>n;1=>1;2=>n+1;3=>0
def computeXOR(n):
    return n if n%4==0 else 1 if n%4==1 else n+1 if n%4==2 else 0
print(computeXOR(6))

# check if x is power of 2
# If number N is a power of 2, then N & (N-1) == 0
def isPowerOf2(x):
    return x and (not(x & (x-1)))

# count bits of n
def count_bits(n):
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt
def count_bits1(n):
    return bin(n).count("1")
print(count_bits(6), count_bits1(6))

# binary string to int
print(int("01001111", 2))

