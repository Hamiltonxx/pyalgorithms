from collections import defaultdict
def longest_equal_subarray(nums, k):
    d = defaultdict(list)
    for i,x in enumerate(nums):
        d[x].append(i)

    ans = 0
    for num,idxs in d.items():
        n = len(idxs)
        l = 0
        for r in range(n):
            # end - start + 1 - cnt <= k
            # while (idxs[r] - idxs[l] + 1) - (r - l + 1) > k:
            while (idxs[r] - idxs[l]) - (r - l) > k:
                l += 1
            ans = max(ans, r-l+1)

    return ans

nums = [1,3,2,3,1,3,4,2,3,2,1,1]
k = 4
print(longest_equal_subarray(nums, k))