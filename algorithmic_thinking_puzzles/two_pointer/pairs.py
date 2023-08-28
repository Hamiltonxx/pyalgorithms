nums = [1,2,3,4,5,20,30,40,50]
def count_pairs_sum_target(nums, target): 
    n = len(nums)
    nums.sort()
    l,r = 0,n-1
    cnt = 0
    while l < r:
        if nums[l] + nums[r] > target:
            cnt += r - l 
            r -= 1
        else:
            l += 1
    return cnt
