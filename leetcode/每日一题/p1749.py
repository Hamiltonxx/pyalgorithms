# 连续子数组和的绝对值的最大值
# 状态转移方程: f[i] = max(f[i-1]+nums[i], nums[i]) = max(f[i-1],0)+nums[i]
def maxabssum(nums):
    ans = f_max = f_min = 0
    for x in nums:
        f_max = max(f_max, 0) + x 
        f_min = min(f_min, 0) + x 
        ans = max(ans, f_max, -f_min)
    return ans

nums = [1,-3,2,3,-4]
print(maxabssum(nums))