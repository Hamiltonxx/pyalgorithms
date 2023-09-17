def min_op(nums):
    n = len(nums)
    def lis_length(n, nums):
        dp = [1] * n
        mx = 1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>=nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            mx = max(mx, dp[i])
        return mx
    return n - lis_length(n,nums)

nums = [2,1,3,2,1]
# nums = [1,3,2,1,3,3]
print(min_op(nums))
