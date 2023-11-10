def majorityElement(nums):
    cnt, can = 0, 0
    for num in nums:
        if cnt == 0:
            can = num
        if can == num:
            cnt += 1
        else:
            cnt -= 1
    return can