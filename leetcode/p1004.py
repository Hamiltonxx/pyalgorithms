# def longestOnes(nums, k):
#     l = mx = 0
#     for r,x in enumerate(nums):
#         if x == 0:
#             k -= 1
#         while k >= 0:
#             if nums[l] == 0:
#                 flips -= 1
#             l += 1
#         mx = max(mx, r-l+1)
#     return mx

def longestOnesV2(nums, k):
    mx = 0
    j = 0
    for i,x in enumerate(nums):
        if x == 0:
            k -= 1
        while k == -1:
            if nums[j] == 0:
                k = 0
            j += 1
        mx = max(mx, i-j+1)
    return mx

# def longestOnesV3(nums, k):
#     l = mx = zeros = 0
#     for r,x in enumerate(nums):
#         if x == 0:
#             zeros += 1
#         while zeros > k:
#             if nums[l] == 0:
#                 zeros -= 1
#             l += 1
#         mx = max(mx, r-l+1)
#     return mx

# 窗口尺寸只增不减
def longestOnesV4(nums, k):
    l = 0
    zeros = 0
    for r,x in enumerate(nums):
        if x == 0:
            zeros += 1
        if zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
    return r - l + 1

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# nums = [0,1,0,1,1,0,0,1,1,1,0,0,0]
# k = 2
print(longestOnesV4(nums,k))