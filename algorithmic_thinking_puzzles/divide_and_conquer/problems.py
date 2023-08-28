# 找数组的最大最小值
def find_max_min(arr, low, high):
    if low == high: # 数组只有一个元素
        return arr[low], arr[low]
    if high == low + 1: # 数组有两个元素
        return min(arr[low],arr[high]), max(arr[low],arr[high])
    # divide the array into two halves
    mid = (low + high) // 2
    min1, max1 = find_max_min(arr, low, mid)
    min2, max2 = find_max_min(arr, mid+1, high)
    return min(min1, min2), max(max1, max2)

arr = [9,3,5,2,4,7,8]
print(find_max_min(arr,0,len(arr)-1))
