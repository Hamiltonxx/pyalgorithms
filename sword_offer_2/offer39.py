# 把众数计+1,其他数计-1,sum>0
# def major(nums):
#     count, candidate = 0, None
#     for x in nums:
#         if count==0:
#             candidate = x
#         count += 1 if candidate==x else -1
#     return candidate

# from collections import defaultdict
# def major(nums):
#     d = defaultdict(int)
#     for x in nums:
#         d[x] += 1
#         if d[x] > len(nums)/2:
#             return x

from collections import Counter
def major(nums):
    c = Counter(nums)
    return max(c, key=c.get)

print(major([1, 2, 3, 2, 6, 2, 2, 2, 4])) 
