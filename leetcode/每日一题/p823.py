import math
def numFactoredBinaryTree(arr):
    arr.sort()
    d = {x:1 for x in arr}
    n = len(arr)
    
    for i in range(1, n):
        for j in range(i):
            if arr[i]/arr[j] < 2 or arr[i-1] ** 2 < arr[i]:
                break
            if arr[i]/arr[j] in d:
                d[arr[i]] += d[arr[j]] * d[arr[i]/arr[j]]

    return sum(d.values())

# arr = [2,4,5,10]
arr = [2,18,3,6]
arr = [2,3,6,18]
print(numFactoredBinaryTree(arr))