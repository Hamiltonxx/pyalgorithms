# def max_sum_contiguous_subarray(nums):
#     a = nums[0]
#     res = a
#     for x in nums[1:]:
#         if a > 0:
#             a += x
#         else:
#             a = x
#         res = max(a,res)
#     return res

# # a = [2,-4,3,-1,2,-4,3]
# a = [-2,11,-4,13,-5,-2]
# print(max_sum_contiguous_subarray(a))

def max_sum_contiguous_subarray(a):
    res = tmp = a[0]
    for x in a[1:]:
        if tmp > 0:
            tmp += x 
        else:
            tmp = x
        res = max(res,tmp)
    return res 

print(max_sum_contiguous_subarray([-2,11,-4,13,-5,-2]))