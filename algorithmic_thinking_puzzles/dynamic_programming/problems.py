# Maximum Value Contiguous Subsequence 子数组的最大和
# [-2,11,-4,13,-5,2] -> 20   [1,-3,4,-2,-1,6] -> 7
# 状态转移方程: mx = max(mx(arr[:i]) + arr[i], 0)
nums = [-2,11,-4,13,-5,2]
# nums = [100,-3,4,-2,-1,6]
# nums = [-3,-2,-1,-8,-9]
def maxSubSum(nums):
    maxsum = -float('inf')
    cursum = 0
    for x in nums:
        cursum = max(x, cursum+x)
        maxsum = max(cursum, maxsum)
    return maxsum
print(maxSubSum(nums))



# 修改一下，使之返回起始和终止元素下标
def maxSubSumidx(nums):
    if not nums:
        return 0, None, None
    cursum = mx = nums[0]
    startidx = endidx = 0
    for i in range(1,len(nums)):
        if nums[i] > cursum + nums[i]:
            cursum = nums[i]
            startidx = i
        else:
            cursum += nums[i]

        if cursum > mx:
            mx = cursum
            endidx = i
    return mx, startidx, endidx

def max_sub_sum(nums):
    maxsum = -float('inf')
    cursum = 0
    for x in nums:
        cursum = max(x, cursum+x)
        maxsum = max(maxsum, cursum)
    return maxsum 

def max_sub_sum_idx(nums):
    maxsum = -float('inf')
    cursum = 0
    n = len(nums)
    start = end = 0
    for i in range(n):
        if cursum < 0:
            cursum = nums[i]
            start = i
        else:
            cursum = cursum + nums[i]

        if maxsum < cursum:
            maxsum = cursum
            end = i
    return maxsum, start, end

# print(maxSubSum(nums))
print(max_sub_sum_idx(nums))

# 非连续子序列的最大和, 不能选择相邻的两个数
# 状态转移方程 M(i) = max{M(i-2)+nums[i], M(i-1)}
def max_non_contiguous_sub(nums):
    n = len(nums)
    if n < 3:
        return max(nums)
    dp = [nums[0], max(nums[0],nums[1])] + [0] * (n-2)
    for i in range(2, n):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    return dp[-1]

nums = [-2,3,-16,100,-4,5]
print("max_non_contiguous_sub")
print(max_non_contiguous_sub(nums))

# 非连续子序列的最大和, 不能选择相邻的三个数
# 状态转移方程 M(i) = max{nums[i]+nums[i-1]+M(i-3), nums[i]+M(i-2), M(i-1)}

# Longest Increasing Subsequence
# 最长的严格递增的子序列
def lis_length(nums):
    n = len(nums)
    dp = [1] * n
    mxlen = 1

    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
        mxlen = max(mxlen, dp[i])
    
    return mxlen

# 上面的时间复杂度为O(N^2),下面用二分把时间复杂度降为O(NlogN)
import bisect
def lis_len(nums):
    piles = []
    for num in nums:
        pile = bisect.bisect_left(piles, num)
        # 如果非严格递增，则用bisect_right 或 bisect
        if pile == len(piles):
            piles.append(num)
        else:
            piles[pile] = num
    return len(piles)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# nums = [3, 10, 2, 1, 20]
# nums = [50, 3, 10, 7, 40, 80]
print(lis_length(nums))
print(lis_len([7,7,7,7,7]))


# 整数背包问题
weights = [2, 3, 4, 5]
values = [3.1, 4, 5, 8]
capacity = 10

for w,v in zip(weights,values):
    print(v/w)

# 0-1背包
# dp[i][j]表示下标为0~(i-1)的物品放进容量为j的背包，最大价值总和
# 递推: dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
def knapsack_01(weight, value, capacity):
    n = len(weight)
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    
    for i in range(1, n+1): # 先遍历物品
        for j in range(1, capacity+1): # 再遍历背包
            if weight[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + value[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][capacity]

# 用一维数组(滚动数组)解决01背包
# dp[j]表示背包容量为j时可以获得的最大价值
# def knapsack01(weight, value, capacity):
#     n = len(weight)
#     dp = [0] * (capacity + 1)

#     for i in range(n):
#         for j in range(capacity, weight[i]-1, -1):
#             dp[j] = max(dp[j], value[i]+dp[j-weights[i]])

#     return dp[capacity]

def knapsack01(weight, value, capacity):
    dp = [0] * (capacity+1)
    for w,v in zip(weight, value):
        for j in range(capacity, w-1, -1):
            dp[j] = max(dp[j], dp[j-w]+v)
    return dp[capacity]

print(knapsack01(weights,values,capacity))

# 完全背包
# def knapsackinf(weight, value, capacity):
#     n = len(weight)
#     dp = [0] * (capacity + 1)
#     for i in range(n):
#         for j in range(weight[i], capacity+1):
#             dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
#     return dp[capacity]

def knapsackinf(weight, value, capacity):
    dp = [0] * (capacity+1)
    for w,v in zip(weight, value):
        for j in range(w, capacity+1):
            dp[j] = max(dp[j], dp[j-w]+v)
    return dp[capacity]

# values = [60, 100, 120] 
# weights = [10, 20, 30] 
# capacity = 50
print(knapsackinf(weights, values, capacity))


# 找零钱问题
def makingChange(amount, denominations):
    dp = [0] + [float('inf')] * amount 

    for i in range(1, amount+1):
        for d in denominations:
            if d <= i:
                dp[i] = min(dp[i], dp[i-d]+1)

    return -1 if dp[amount]==float('inf') else dp[amount]

amount = 20
denominations = [7,11]

print(makingChange(amount, denominations))

# 堆箱子问题
boxes = [(1,2,3),(2,3,4),(3,4,5)]
def box_stack_height(boxes):
    rotations = []
    for l,w,h in boxes:
        rotations += [(l,w,h),(w,l,h),(h,l,w)]
    rotations.sort(key=lambda x:x[0]*x[1], reverse=True)

    n = len(rotations)
    dp = [0] * n 

    for i in range(n):
        dp[i] = rotations[i][2]
        for j in range(i):
            if rotations[j][0] > rotations[i][0] and rotations[j][1] > rotations[j][1]:
                dp[i] = max(dp[i], dp[j]+rotations[i][2])

    return max(dp)
        
print('Maximum height:', box_stack_height(boxes))

# 印度桥问题
# 左 [1,2,...,n] 右 [3,n,...,2],相同序号数字可以建桥，桥不能交叉，求最多桥数
# 可以转换为LIS问题

# Subset Sum
# n个正数集合里选子集，使之和为T, [3,2,4,19,3,7,13,10,6,11]
# 可以转换为背包问题
# dp[i][j]定义为前i个元素和为j
# 状态转移方程 dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
# def subset_sum(nums, target):
#     n = len(nums)
#     dp = [[False] * (target+1) for _ in range(n+1)]
#     dp[0][0] = True

#     for i in range(1, n+1):
#         dp[i][0] = True
#         for j in range(1, target+1):
#             if j < nums[i-1]:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
#     return dp[n][target]
# 更精简的写法
def exist_subset_sum(nums, target):
    # dp[i]定义为存在子集和为i
    dp = [False] * (target+1)
    dp[0] = True

    for num in nums:
        for i in range(target, num-1, -1):
            dp[i] = dp[i] or dp[i-num]

    return dp[target]


A = [3,2,4,19,3,7,13,10,6,11]
T = 17
print(exist_subset_sum(A,T))


# 编辑距离问题 把字符串A转换成字符串B的最小操作数，可以增、删、改A的字符
def editDistance(stra, strb):
    m = len(stra)
    n = len(strb)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i 
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if stra[i-1] == strb[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)

    return dp[m][n]

print(editDistance("kitten","sitting"))
        
# 最长回文子序列
# A,G,C,T,C,B,M,A,A,C,T,G,G,A,M -> A G T C A A C T G A  len=10
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

def lcs(s1, s2):
    d, a = defaultdict(list), []
    for i,x in enumerate(s2):
        d[x].append(i)
    for x in s1:
        if x in d:
            for i in reversed(d[x]):
                idx = bisect.bisect_left(a, i)
                if idx == len(a):
                    a.append(i)
                else:
                    a[idx] = i
    return len(a)

# s = "AGCTCBMAACTGGAM"
s = "BBABCBCAB"
print(longest_palindromic_subsequence(s))


# 最长公共子序列 bisect
from collections import defaultdict
import bisect
def lcs(s1, s2):
    d, a = defaultdict(list), []
    for i,x in enumerate(s2):
        d[x].append(i)
    for x in s1:
        if x in d:
            for i in reversed(d[x]):
                idx = bisect.bisect_left(a, i)
                if idx == len(a):
                    a.append(i)
                else:
                    a[idx] = i
    return len(a)

# 最长公共子串
def lcsa(s1, s2):
    pass