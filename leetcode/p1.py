def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return i, d[target-nums[i]]
        else:
            d[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

