# def lcs(nums1, nums2):
#     m, n = len(nums1), len(nums2)
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     mx = 0
    
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if nums1[i-1] == nums2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#                 mx = max(mx, dp[i][j])
#     return mx

def lcsa(nums1, nums2):
    s2 = ''.join([chr(x) for x in nums2])
    com, mx = '', 0
    for num in nums1:
        com += chr(num)
        if com in s2:
            mx = max(mx, len(com))
        else:
            com = com[1:]
    return mx


nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
# nums1 = [0,0,0,0,0]
# nums2 = [0,0,0,0,0]
# nums1 = [0,1,1,1,1]
# nums2 = [1,0,1,0,1]


print(lcsa(nums1, nums2))