def twentyone(array, num=21):
    if num<0:
        return 
    if len(array)==0:
        if num==0:
            yield []
        return
    for solution in twentyone(array[1:],num):
        yield solution
    for solution in twentyone(array[1:],num-array[0]):
        yield [array[0]] + solution

print(list(twentyone([5,16,5,11,7,9])))