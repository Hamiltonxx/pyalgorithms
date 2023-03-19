# list argument must be sorted in ascending order.

import bisect 
a = [2, 4, 6, 8, 10, 12, 14]
x = 7
i = bisect.bisect_left(a,x)
print(i)
a.insert(i, x)
print(a)
b = [2, 4, 6, 8, 8, 8, 10, 12, 14]
x = 8
i = bisect.bisect_left(b,x)
print(i)
a = [1, 3, 5, 6, 7, 9, 10, 12, 14]
x = 8
i = bisect.bisect_left(a, x, lo=2, hi=7) # [5,6,7,9,10]
print(i)
a = [1, 2, 3, 4, 4, 7, 6]
x = 4
i = bisect.bisect_right(a, x)
print(i)

a = [2, 4, 6, 6, 8, 8, 8, 10, 12, 14]
x = 8
bisect.insort_left(a, x)
print(a)
y = 6
bisect.insort_right(a, y)
print(a)