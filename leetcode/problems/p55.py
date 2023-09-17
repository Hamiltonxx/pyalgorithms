def canJump(nums):
    n = len(nums)
    i = j = n-1
    for i in range(n-2,-1,-1):
        if nums[i] >= j-i:
            j = i
    return j == 0
