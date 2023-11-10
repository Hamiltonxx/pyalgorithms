def removeDuplicates(nums):
    i, n = 2, len(nums)
    if n <= 2: return n
    for j in range(2, n):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    return i

# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))