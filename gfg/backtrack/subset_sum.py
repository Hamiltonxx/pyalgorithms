def subset_sum(arr,num):
    if num < 0: 
        return 
    if len(arr)==0:
        if num==0:
            yield []
        return 
    for solution in subset_sum(arr[1:],num):
        yield solution
    for solution in subset_sum(arr[1:],num-arr[0]):
        yield [arr[0]] + solution

arr = [16,5,11,7,9]
print(list(subset_sum(arr,21)))