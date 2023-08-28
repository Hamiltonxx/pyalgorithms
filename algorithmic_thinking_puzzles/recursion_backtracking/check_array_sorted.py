# Given an array, check whether the array is in sorted order with recursion

def is_array_sorted(A):
    if len(A)==1:
        return True 
    return A[0]<=A[1] and is_array_sorted(A[1:])
A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
print(is_array_sorted(A))