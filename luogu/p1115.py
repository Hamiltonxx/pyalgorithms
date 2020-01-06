def max_sum_configuous_subarray(a):
    res = tmp = a[0]
    for x in a[1:]:
        if tmp > 0:
            tmp += x 
        else:
            tmp = x
        res = max(res,tmp)
    return res 

input()
a = list(map(int,input().split()))
print(max_sum_configuous_subarray(a))