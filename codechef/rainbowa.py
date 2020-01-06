t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    if set(lst)=={1,2,3,4,5,6,7} and lst==lst[::-1]:
        print("yes")
    else:
        print("no") 
