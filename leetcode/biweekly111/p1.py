def countPairs(nums, target):
    n = len(nums)
    total = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] < target:
                total += 1
    return total