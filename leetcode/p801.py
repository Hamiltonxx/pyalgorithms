# def minSwap(a, b):
    # dp[i] 定义为: nums1[i]和nums2[i]之前的最小操作数
    # n = len(nums1)
    # dp = [0] * n
    # for i in range(1,n):
    #     if nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1]:
    #         dp[i] = dp[i-1]
    #     else:
    #         nums1[i],nums2[i] = nums2[i],nums1[i]
    #         dp[i] = dp[i-1] + 1
    # return dp[n-1]

    # n = len(a)
    # noswap = [0] * n 
    # swap = [1] * n 
    # for i in range(1,n):
    #     inc = a[i] > a[i-1] and b[i] > b[i-1]
    #     incx = a[i] > b[i-1] and b[i] > a[i-1]
    #     if inc and incx:
    #         swap[i] = min(noswap[i-1], swap[i-1]) + 1
    #         noswap[i] = min(noswap[i-1], swap[i-1])
    #     elif inc: # can't swap
    #         swap[i] = swap[i-1] + 1 # 如果i调换，则i-1也得调换
    #         noswap[i] = noswap[i-1]
    #     elif incx: # must swap:
    #         swap[i] = noswap[i-1] + 1
    #         noswap[i] = swap[i-1]
    # return min(swap[n-1], noswap[n-1])


# sm: 统计 x < y 的次数; lg: 统计 x > y 的次数
# ans = min(sm, lg)
# 当遇到 max(A[i-1],B[i-1]) < min(A[i],B[i]) 时，重新开始计数(既不需要sm+1,也不需要lg+1)
# 如 A = [1,3,5,4,8]; B = [1,2,3,7,9]
# ans = i-1之前的最小值 + i之后的最小值
# 返回各段最小值之和
def minSwap(nums1, nums2):
    ans = sm = lg = mx = 0
    for x,y in zip(nums1, nums2):
        if mx < min(x, y):
            ans += min(sm, lg)
            sm = lg = 0
        if x < y: sm += 1
        elif x > y: lg += 1
        mx = max(x, y)
    return ans + min(sm, lg)

        


            