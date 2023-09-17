# def wiggleMaxLength(nums):
#     ans = nums[:1]
#     inc = 0
#     for num in nums[1:]:
#         if inc:
#             if (num - ans[-1]) * inc < 0:
#                 ans.append(num)
#             elif (num - ans[-1]) * inc > 0:
#                 ans[-1] = num
#         else:
#             if num - ans[-1]:
#                 ans.append(num)
#                 inc = num - ans[-1]
#     print(ans, end='  ')
#     return len(ans)

def up_and_down(nums):
    up = down = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 0:
            up = down + 1
        if nums[i] - nums[i-1] < 0:
            down = up + 1
        # difference between ups and downs is always 1 or 0
    return max(up, down) + 1

    
