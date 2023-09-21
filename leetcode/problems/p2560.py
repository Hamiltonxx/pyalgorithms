# 长度至少为k的不相邻子序列A的最大值的最小值min(max(A))
import bisect
def minCapability(nums, k):
    def mxhouse(mx): # 最大金额为mx时，最多可以偷多少间
        pre, cur = 0, 0
        for num in nums:
            if num > mx:
                pre = cur
            else:
                pre, cur = cur, max(pre+1, cur)
        return cur 
    return bisect.bisect_left(range(10**9), k, key=mxhouse)