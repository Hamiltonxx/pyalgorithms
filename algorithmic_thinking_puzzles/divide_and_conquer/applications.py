# Finding peak element, A[i-1]<=A[i]>=A[i+1], assume A[-1]=A[n]=-inf
# Finding all peaks with linear search
def findPeaks(arr):
    arr = [-float('inf')] + arr + [-float('inf')]
    peaks = []
    for i in range(1,len(arr)-1):
        if arr[i-1]<=arr[i]>=arr[i+1]:
            peaks.append(arr[i])
    return peaks

def find_peak(arr, low, high):
    if low == high:
        return low
    mid = (low+high)//2
    if arr[mid-1] <= arr[mid] >= arr[mid+1]:
        return mid
    if arr[mid-1] > arr[mid]:
        return find_peak(arr, low, mid-1)
    return find_peak(arr, mid+1, high)

arr = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]
print(findPeaks(arr))

print(find_peak(arr,0,len(arr)-1))
