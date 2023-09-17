# def candy(nums):
#     up, down, peak = 0, 0, 0
#     ans = len(nums)
    
#     for i in range(len(nums)-1):
#         if nums[i+1] > nums[i]:
#             up, down, peak = up+1, 0, up+1
#             ans += up
#         elif nums[i+1] < nums[i]:
#             up, down = 0, down+1
#             ans += down - 1 + int(down>=peak)
#         else:
#             up, down, peak = 0, 0, 0

#     return ans


def candy(ratings):
    n = len(ratings)
    ans = [1] * n
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            ans[i] = ans[i-1]+1
    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1] and ans[i+1]+1 > ans[i]:
            ans[i] = ans[i+1] + 1
    return sum(ans)
        
        
