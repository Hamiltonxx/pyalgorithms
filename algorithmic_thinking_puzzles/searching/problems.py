# 判断一个数组是否有重复元素
def check_duplicates(arr):
    return len(arr) == len(set(arr))
A = [3,2,10,20,22,32]
print(check_duplicates(A))
A = [3,2,1,2,2,3]
print(check_duplicates(A))

# 找出数组中出现次数最多的元素
from collections import Counter
def find_most_common_elements(arr):
    counter = Counter(arr)
    most_common_list = counter.most_common(1)
    return most_common_list[0][0]
print(find_most_common_elements(A))

# Find the first element in an array that is repeated.
def find_first_repeated_element(arr):
    seen = set()
    rep = set()
    for x in arr:
        if x in seen:
            rep.add(x)
        else:
            seen.add(x)
    for x in arr:
        if x in rep:
            return x 
    return None
print(A)
print("第一个重复元素:",find_first_repeated_element(A))

# We are given a list of n-1 integers and these integers are in the range of 1 to n. 
# There are no duplicates in the list. One of the integers is missing in the list. 
# Given an algorithm to find the missing integer.
# 另一种表述
# There is an array of numbers. 
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.
a = [4, 7, 2, 11, 9]
a_shuffle = [11,2,9,4]
def find_missing_element(a,b):
    return sum(a) - sum(b)
print(find_missing_element(a,a_shuffle))

def find_missing_number(arr1, arr2):
    result = 0
    for x in arr1:
        result ^= x 
    for x in arr2:
        result ^= x 
    return result
print(find_missing_number(a, a_shuffle))

# Find the Number occurring an Odd Number of Times
arr = [1, 2, 3, 2, 3, 1, 3]
def find_occurring_odd_times(arr):
    result = 0
    for x in arr:
        result ^= x
    return result
print(find_occurring_odd_times(arr))

# Find the two repeating elements in a given array
# 待好好理解xor与位运算
# 数学方法是 X+Y = sum(A)-sum(B) X*Y = Prod(A)/Prod(B)
# 令sum=A,Prod=B,则X=(A+sqrt(A**2-4*B))/2, Y=(A-sqrt(A**2-4*B))/2
arr1 = [3,6,7,7,8,9,9,10]
arr2 = [3,6,7,8,9,10]
from math import sqrt
def find_two_repeating_number(arr1,arr2):
    A = sum(arr1)-sum(arr2)
    B = 1
    for x in arr1:
        B *= x 
    for x in arr2:
        B //= x
    X = (A+sqrt(A**2-4*B))/2
    Y = (A-sqrt(A**2-4*B))/2
    return int(X),int(Y)
print(find_two_repeating_number(arr1,arr2))

# Given an array of elements. 
# Find two elements in the array such that their sum is equal to given number K.
arr = [3,1,7,9,2]
K = 10
def find_two_number_sum_K(arr,K):
    d = {}
    results = []
    for x in arr:
        if K-x in d:
            results.append((x,K-x))
        else:
            d[x] = K-x 
    return results
print(find_two_number_sum_K(arr,K))

# Given an array with both positive and negative numbers, 
# find the two elements such that their sum is closest to zero.
# 使用双指针方法
def find_elements_sum_closeset_to_zero(arr):
    arr.sort()
    n = len(arr)
    left = 0
    right = n-1
    closest_sum = float('inf')
    closest_pair = None 

    while left < right:
        curr_sum = arr[left] + arr[right]

        if abs(curr_sum) < abs(closest_sum):
            closest_sum = curr_sum 
            closest_pair = (arr[left], arr[right])

        if curr_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair

arr = [1, 60, -10, 70, -80, 85]
print(find_elements_sum_closeset_to_zero(arr))

arr = [1, 3, 5, 7, 9, 6, 4, 2]
def find_peak_element(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return arr[i]
    return arr[n-1]
arr = [3,3,3]
print(find_peak_element(arr))

def find_peak_index(arr):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid-1]<=arr[mid]>=arr[mid+1]:
            return mid
        if arr[mid-1]<=arr[mid]<=arr[mid+1]:
            low = mid+1
        else:
            high = mid-1
print("Find PEAK",find_peak_index([1, 3, 5, 7, 9, 6, 4, 2]))
print("Find PEAK",find_peak_index([1, 3, 9, 8, 7, 6, 4, 2]))
        

# 1111......11110000......0000
# find the index where 0's start
def find_zero_start_index(s):
    low = 0
    high = len(s)-1
    while low <= high:
        mid = (low+high)//2
        if s[mid] == "1":
            low = mid+1
        else:
            high = mid-1
    return low
print(find_zero_start_index("111110000"))

# an sorted array rotated unkown times, find an element
# arr = [15,16,19,20,25,1,3,4,5,7,10,14]
arr = [10,14,15,16,19,20,25,1,3,4,5,7]
def search_rotated_array(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target<=arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=target<=arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1
print(search_rotated_array(arr,5))

#     def recur(low,high):
#         if low>high:
#             return -1
#         mid = (low+high)//2
#         if arr[mid]==target:
#             return mid
#         if arr[mid]<target:
#             if target < arr[high]:
#                 return recur(mid+1,high)
#             else:
#                 return recur(low,mid-1)
#         else: 
#             if target < arr[0]:
#                 return recur(mid+1,high)
#             else:
#                 return recur(low, mid-1)
        
#     result = recur(0,len(arr)-1)
#     return result
# print(search_rotated_array(arr,16))


