# 问题转化为: 给定一个大小为3N的整数数组，选择N个不相邻的整数，使其和最大。(首尾视为相邻)
from functools import cache
def maxSizeSlices(slices):
    n = len(slices)
    @cache
    def optimal(i, p, end):
        if i >= end or p == 0:
            return 0
        take = slices[i] + optimal(i+2, p-1, end)
        dont = optimal(i+1, p, end)
        return max(take, dont)
    return max(optimal(0, n//3, n-1), optimal(1, n//3, n))