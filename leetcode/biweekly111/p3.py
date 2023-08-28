def minop(nums):
    # n = len(nums)
    ans = 0
    for idx1 in range(len(nums)-1,-1,-1):
        if nums[idx1]==1:
            ans += idx1+1 - nums.count(1)
            nums = nums[idx1+1:]
            break

    for idx2 in range(len(nums)-1,-1,-1):
        if nums[idx2]==2:
            cnt3 = idx2+1 - nums.count(2)
            break
    if 3 in nums:
        idx3 = nums.index(3)
        cnt2 = nums[idx3:].count(2)
        ans += min(cnt3, cnt2)
    return ans

# nums = [2,1,3,2,1]
# nums = [1,3,2,1,3,3]
nums = [2,2,2,2,3,3]
print(minop(nums))

    # else:
    #     # no 1
    #     pass 

    # idx1 = n-1
    # while idx1>=0:
    #     if nums[idx1]!=1:
    #         idx1 -= 1
    #     else:
    #         break
    
