def maxNonDescreasingLength(nums1, nums2):
    n = len(nums1)
    dp1 = [1 for _ in nums1]
    dp2 = [1 for _ in nums2]

    for i in range(n-2,-1,-1):
        if nums1[i] <= nums1[i+1]:
            dp1[i] = max(dp1[i], dp1[i+1]+1)
        if nums1[i] <= nums2[i+1]:
            dp1[i] = max(dp1[i], dp2[i+1]+1)
        if nums2[i] <= nums1[i+1]:
            dp2[i] = max(dp2[i], dp1[i+1]+1)
        if nums2[i] <= nums2[i+1]:
            dp2[i] = max(dp2[i], dp2[i+1]+1)

    return max(max(dp1), max(dp2))
