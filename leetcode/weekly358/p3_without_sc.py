import bisect 
def minAbsoulteDifference(nums,x):
    n = len(nums)
    arr = [] 
    i = 0
    j = x
    mn = float('inf')

    while j < n:
        bisect.insort(arr,nums[i])
        idx_j = bisect.bisect(arr, nums[j])
        if idx_j == 0:
            mn = min(mn, abs(nums[j]-arr[0]))
        elif idx_j == len(arr):
            mn = min(mn, abs(nums[j]-arr[-1]))
        else:
            mn = min(mn, abs(nums[j]-arr[idx_j]), abs(nums[j]-arr[idx_j-1]))

        i += 1
        j += 1

    return mn

nums = [5,3,2,10,15,7,9]
x = 2
print(minAbsoulteDifference(nums,x))