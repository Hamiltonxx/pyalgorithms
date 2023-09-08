# binary representation of n
def bin_repr(n, INT_BITS=32):
    return bin(n)[2:].zfill(INT_BITS)
print(bin_repr(7))

# count set bits
def count_bits(n):
    return bin(n).count("1")
print(count_bits(6))

# add two binary string
def add_binary(a,b):
    return bin(int(a,2)+int(b,2))[2:]

# turn off/unset the rightmost set bit. 12(1100)=>8(1000)
def turn_off_rightmost_bit1(n):
    return n & (n-1)

# left rotate 11100101 by 3: 00101111
def left_rotate(n, d, INT_BITS=32):
    return (n << d) | (n >> (INT_BITS-d))
def right_rotate(n, d, INT_BITS=32):
    return (n >> d) | (n << (INT_BITS-d))

# compute n modulo d without / or %, where d is a power of 2
# 6(110)%4(100)=2, 12(1100)%8(1000)=4, 10(1010)%2(10)=0
def get_modulo(n,d):
    return n & (d-1)

# find the number occurring odd number of times
nums = [1,2,3,2,3,2,1]
def get_odd_occurrence(nums):
    ans = 0
    for x in nums:
        ans ^= x 
    return ans
print(get_odd_occurrence(nums))

# find position of the only set bit. 2=>2, 5=>-1
def find_position(n):
    if n & (n-1): # not the power of 2
        return -1
    cnt = 0
    while n:
        n >>= 1
        cnt += 1
    return cnt
print(find_position(5))

# swap two variable without using a temporary variable
def xor_swap(a,b):
    a = a ^ b 
    b = a ^ b 
    a = a ^ b 
    return a,b
x, y = 10, 20
print(xor_swap(x,y))

# swap bits. 47(00101111) p1=1,p2=5,n=3 => 227(11100011)
def swap_bits(x, p1, p2, n):
    # 创建掩码
    mask = (1 << n) - 1
    mask1 = mask << p1
    mask2 = mask << p2
    # 提取要交换的位
    bits1 = (x & mask1) >> p1
    bits2 = (x & mask2) >> p2
    # 清除原始数字中要交换的位
    # x &= ~(mask1 | mask2)
    x &= ~mask1 & ~mask2
    # 将交换的位放置在正确的位置
    x |= (bits1 << p2) | (bits2 << p1)

    return x
def swap_bits_xor(x, p1, p2, n):
    xor = ((x >> p1) ^ (x >> p2)) & ((1 << n) - 1)
    return x ^ ((xor << p1) | (xor << p2))
print(swap_bits(47,1,5,3))
print(swap_bits_xor(47,1,5,3))

# smallest power of 2 greater than or equal to n 
# 8=>8, 9=>16, 7=>8
def next_power_of_2(n):
    if not (n & (n-1)):
        return n
    return int("1"+(len(bin(n))-2)*"0", 2)
def next_power_of_2_shift(n):
    p = 1
    while p < n:
        p <<= 1
    return p
print(next_power_of_2_shift(8))
print(next_power_of_2_shift(11))

# get parity: odd number of 1 => odd, otherwise => even
def get_parity(n):
    return bin(n).count("1") % 2
print("get parity",get_parity(6))

# check sparse number: no two or more consecutive bits are set in it's binary.
def is_sparse_number(n):
    return not n & (n >> 1)
print(is_sparse_number(6))
print(is_sparse_number(5))

# copy set bits in a range: x=10,y=13,l=2,r=3  10 -> y[2:3] -> 14 稍有疑问
def copy_set_bits(x, y, l, r):
    mask = (1 << (r-l+1) - 1) << (l-1)
    bits = y & mask 
    return x | bits
print(copy_set_bits(10,13,2,3)) # 1010  1101

#* next higher number with same number of set bits.
def next_higher_number_same_ones(x):
    rightmost_1 = x & -x 

    next_higher_one_bit = x + rightmost_1

    right_ones_pattern = x ^ next_higher_one_bit
    right_ones_pattern = right_ones_pattern // rightmost_1
    right_ones_pattern = right_ones_pattern >> 2

    next = next_higher_one_bit | right_ones_pattern

    return next

def next_higher_number_same_ones_v2(x):
    b = "0"+bin(x)[2:]
    r1 = b.rindex("1")
    # 0要在1前
    r0 = b[:r1].rindex("0")
    c1 = b[r0:].count('1')
    ans = b[:r0] + "1" + "0"*(len(b)-r0-c1) + "1"*(c1-1)
    return int(ans, 2)

print("next higher number")
x = int("1101001",2)
print(next_higher_number_same_ones(x)) 
print(next_higher_number_same_ones_v2(x))

#* Find the maximum subarray xor in a given array
def find_max_xor_sum(nums):
    max_xor_sum = 0
    xor_prefix = 0
    trie = {}

    for num in nums:
        # 更新前缀异或值
        xor_prefix ^= num
        # 插入前缀异或值到字典树
        h = trie
        for i in range(31, -1, -1):
            bit = (xor_prefix >> i) & 1
            h = h.setdefault(bit, {})

        # 计算当前前缀异或值与字典树中的最大异或值
        h = trie
        curr_xor_sum = 0
        for i in range(31, -1, -1):
            bit = (xor_prefix >> i) & 1
            if 1-bit in h:
                h = h[1-bit]
                curr_xor_sum |= (1 << i)
            else:
                h = h[bit]
        max_xor_sum = max(max_xor_sum, curr_xor_sum)

    return max_xor_sum

# nums = [3, 10, 5, 25, 2, 8]
nums = [1,2,3,4]
# nums = [8, 1, 2, 12, 7, 6]
# nums = [4, 6]
max_xor_sum = find_max_xor_sum(nums)
print(max_xor_sum)  

# Find longest sequence of 1's in binary representation with one flip
# def longest_sequence_with_one_flip_v3(num):
#     l = r = flips = mx = 0
#     b = bin(num)[2:]
#     for r in range(len(b)):
#         if b[r] == '0':
#             flips += 1
#         while flips > 1:
#             if b[l] == '0':
#                 flips -= 1
#             l += 1
#         mx = max(mx, r-l+1)
#     return mx
# 滑动窗口尺寸只增不减
def longest_sequence_with_one_flip(num):
    l = 0
    zeros = 0
    b = bin(num)[2:]
    for r,x in enumerate(b):
        if x == '0':
            zeros += 1
        if zeros > 1:
            if b[l] == '0':
                zeros -= 1
            l += 1
    return r - l + 1
print("longest_sequence_with_one_flip")
print(longest_sequence_with_one_flip(15))
print(longest_sequence_with_one_flip(1775))
print(longest_sequence_with_one_flip(7))
# 看看和下面这个问题的区别(找长度和找index的区别)
# Find index of 0 to be replaced with 1 to get longest continuous sequence of 1s
# [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1] => 9   [1, 1, 1, 1, 0] => 4
def indexof0(b):
    b.append(0)
    mxidx = 0
    mx = 1
    pre = prepre = -1
    for i,x in enumerate(b):
        if x == 0:
            if i - prepre - 1 > mx:
                mx = i - prepre - 1
                mxidx = pre
            prepre = pre
            pre = i
    return mxidx
# b = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
b = [1, 1, 1, 1, 0]
print(indexof0(b))

# Closest/Next smaller and greater numbers with same number of set bits.
# 1. zero-to-one flip + one-to-zero flip
# 2. next greater: (最右)0在(最右)1前; next smaller: (最右)1在(最右)0前





