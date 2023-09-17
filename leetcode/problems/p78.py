from typing import List 
from itertools import combinations, chain
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # for i in range(len(nums)+1):
        #     ans += list(combinations(nums,i))
        # return ans

        # return list(chain(*[combinations(nums,i) for i in range(len(nums)+1)]))

        n = len(nums)
        ans = []
        for mask in range(1 << n):
            subset = []
            copy = mask
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            ans.append(subset)
        return ans