from functools import lru_cache
def findTargetSumWays(nums, target):
    @lru_cache(None)
    def count(idx=0, partial=0):
        if idx==len(nums):
            return 1 if partial==target else 0
        cnt_add = count(idx+1, partial+nums[idx])
        cnt_sub = count(idx+1, partial-nums[idx])
        return cnt_add + cnt_sub 
    return count()

from collections import Counter, defaultdict
def expressions_sum(nums, target):
    d = {0:1}
    for num in nums:
        tmp = {}
        for key in d:
            tmp[key+num] = tmp.get(key+num, 0) + d[key]
            tmp[key-num] = tmp.get(key-num, 0) + d[key]
        d = tmp
    return d.get(target, 0)

print(expressions_sum([1,1,1,1,1],3))
    

