def jump(nums):
    mx = j = cnt = 0

    for i in range(len(nums)-1):
        mx = max(mx, i+nums[i])
        if i == j:
            j = mx
            cnt += 1

    return cnt


# nums = [2,3,1,1,4]
nums = [2,1,3,7,6,4,2,4]
print(jump(nums))


    
