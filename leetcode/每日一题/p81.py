nums = [2,5,6,0,0,1,2]
# nums = [4,5,6,7,8,9,0,1,2]
# nums = [8,9,0,1,2,3,4,5,6]
nums = [1,1,1,1,2,1]
target = 2
def search_rotated_sorted(nums, target):
    n = len(nums)
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return True
        
        # if nums[left]<=target<nums[mid] or target<nums[mid]<=nums[left] or nums[mid]<=nums[left]<=target:
        if nums[left]<=target<nums[mid] or target<nums[mid]<=nums[right] or nums[mid]<=nums[left]<=target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

print(search_rotated_sorted(nums,target))

# 最后，这题不能在O(log(N))内过，O(N)
# 那就 return target in nums吧