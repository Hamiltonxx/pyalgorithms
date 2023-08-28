def minop(nums, target):
    sm = sum(nums)
    if sm < target:
        return -1
    nums.sort()
    op = 0
    while target:
        a = nums.pop()
        if sm - a >= target:
            sm -= a
        elif a <= target:
            sm -= a
            target -= a
        else:
            nums += [a//2,a//2]
            op += 1

    return op
            
nums = [1,2,8]
target = 7
print(minop(nums,target))