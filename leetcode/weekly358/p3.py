from sortedcontainers import SortedList
nums = [5,3,2,10,15,7,9]
x = 2
# nums = [68,68]
# x = 1

def minAbsoulteDifference(nums,x):
    n = len(nums)
    mn = float('inf')
    sl = SortedList(nums[x-1:])
    for i in range(n-x):
        sl.discard(nums[i+x-1])
        j = sl.bisect_left(nums[i])
        if j==0:
            mn = min(mn, abs(nums[i]-sl[0]))
        elif j==len(sl):
            mn = min(mn, abs(nums[i]-sl[-1]))
        else:
            mn = min(mn, abs(nums[i]-sl[j-1]), abs(nums[i]-sl[j]))
        # for j in range(i+x,n):
        #     mn = min(mn,abs(nums[i]-nums[j]))
    return mn

print(minAbsoulteDifference(nums,x))