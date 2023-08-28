def find_number_pairs(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    pairs = []

    while left < right:
        if arr[left] + arr[right] > target:
            # 找到一个数字对
            pairs.append((arr[left], arr[right]))
            # 继续寻找下一个可能的数字对
            right -= 1
        else:
            # 数字对的和小于等于目标值，继续向右移动左指针
            left += 1

    return pairs

# def find_number_pairs(arr, target):
#     n = len(arr)
#     pairs = []

#     for i in range(n):
#         left = i + 1
#         right = n - 1

#         while left <= right:
#             mid = left + (right - left) // 2

#             if arr[mid] > target - arr[i]:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         # 将所有大于目标值的数字对添加到结果列表中
#         for j in range(i + 1, left):
#             pairs.append((arr[i], arr[j]))

#     return pairs

arr = [1,2,3,4,5,6, 20,30,40,50]
target = 23
print(find_number_pairs(arr,target))

def numberOfPairs(nums,target):
    i = 0
    j = len(nums) - 1
    pairs=0
    while i<j:
        if nums[i]+nums[j]>target:
            pairs += j-i
            j -= 1
        else:
            i += 1
    return pairs

print('no of pairs',numberOfPairs([1, 3, 7, 9, 10, 11],7)) #. output:14
print('no of pairs',numberOfPairs([1, 11],7)) #. output: 1
print('no of pairs',numberOfPairs([0,1],7)) #.output: 0
print('no of pairs',numberOfPairs([0,1,2,2],2)) #  output:5
print('no of pairs',numberOfPairs(arr,target))