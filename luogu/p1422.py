#由于python3浮点数的四舍五入不精确，自己写四舍五入精确一位小数的方法
def myround(x):
    y = x*10
    if y - int(y) < 0.5:
        res = int(y)
    else:
        res = int(y)+1
    return res/10



# N = int(input())

# if N<=150:
#     res = 0.4463 * N 
# elif 151<=N<=400:
#     res = 150*0.4463 + (N-150)*0.4663
# else:
#     res = 150*0.4663 + (400-150)*0.4663 + (N-400)*0.5663

# print("{:.1f}".format(res))
a = [1.25,3.45,10.15,11.15,11.25,11.35,12.35,12.45]
for x in a:
    print(x,round(x,1),myround(x))