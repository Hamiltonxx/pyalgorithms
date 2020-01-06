def multiple3(n):
    if n==1: return 3
    return multiple3(n-1) + 3

print(multiple3(4))

def sum_first(n):
    if n==0: return 0
    return sum_first(n-1) + n

print(sum_first(5))

def pascal_triangle(n):
    if n==1: return [1]
    else:
        nums = pascal_triangle(n-1)
        res = [(x+y) for (x,y) in zip(nums,nums[1:])]
        return [1] + res + [1]

print(pascal_triangle(6))
