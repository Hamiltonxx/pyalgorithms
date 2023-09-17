def findMedianSortedArrays(nums1, nums2):
    if nums1[-1] <= nums2[0]:
        return (nums1[-1]+nums2[0])/2
    if nums2[-1] <= nums1[0]:
        return (nums2[-1]+nums1[0])/2
    