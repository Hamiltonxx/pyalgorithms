def non_consecutive_max_sum(nums):
        pre, cur = 0, nums[0]
        for num in nums[1:]:
            pre, cur = cur, max(pre+num, cur)
        return cur

print(non_consecutive_max_sum([2,3,1]))

def rob(nums):
      pass 
    
    
print(rob([1,2,3,1]))