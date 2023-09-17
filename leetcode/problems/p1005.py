# import bisect
# def largestAfterNegation(nums, k):
#     neg, pos = [], []
#     for num in nums:
#         if num < 0: bisect.insort(neg, num)
#         else: bisect.insort(pos, num)
#     if k <= len(neg):
#         return -sum(neg[:k]) + sum(neg[k:]) + sum(pos)
#     else:
#         sm = -sum(neg) + sum(pos)
#         if (k-len(neg)) & 1: 
#             mn = 0
#             if pos and pos[0]!=0:
#                 if neg:
#                     mn = min(pos[0], neg[-1])
#                 else:
#                     mn = pos[0]
#             else:
#                 if neg:
#                     mn = neg[-1]
#             sm -= 2*mn

#         return sm

def leetcode(nums, k):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
    nums.sort()
    if k > 0 and k & 1:
        nums[0] = -nums[0]
    return sum(nums)

# def leetcode2(nums, k):
#     freq = [0] * 201
#     sm = 0
#     # mx = 0

#     for num in nums:
#         # mx = max(mx, abs(num))
#         freq[100+num] += 1
#         sm += num

#     # if mx == 0:
#     #     return 0
    
#     while k > 0:
#         k -= 1
#         # i = 100 - mx
#         i = 0
#         while freq[i] == 0:
#             i += 1
#         freq[i] -= 1
#         freq[200-i] += 1
#         sm -= 2 * (i - 100)

#     return sm




nums = [4,2,3]
k = 5
nums = [3,-1,0,2]
k = 3
nums = [5,6,9,-3,3]
k = 2


# print(largestAfterNegation(nums, k))
