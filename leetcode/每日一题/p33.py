nums = [4,5,6,7,8,9,0,1,2]
nums = [8,9,0,1,2,3,4,5,6]
# nums = [4,5,6,7,0,1,2]
nums = [5,1,3]
def search_rotated_sorted_array(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid 

        if nums[left]<=target<nums[mid] or target<nums[mid]<=nums[right] or nums[mid]<nums[left]<=target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

print(search_rotated_sorted_array(nums,3))

        