from collections import defaultdict
# def longestEqualSubarray(nums, k):
#     d = defaultdict(list)
#     for num,idx in enumerate(nums):
#         d[num].append(idx)
#     mx = 1
#     for num,lst in d.items():
#         i = j = 0
#         while j < len(lst):
#             if (lst[j]-lst[i]+1) - (j-i+1) > k:
#                 i += 1
#             mx = max(mx, j-i+1)
#     return mx


def longest_equal_subarray(nums, k):
    d = defaultdict(list)
    for i,x in enumerate(nums):
        d[x].append(i)
    mx = 1
    for idxs in d.values():
        # 需要满足 end-start+1 - (r-l+1) <= k 才能操作
        n = len(idxs)
        l = 0
        for r in range(1,n):
            while (idxs[r]-idxs[l]+1) - (r-l+1) > k:
                l += 1
            mx = max(mx, r-l+1)
    return mx



