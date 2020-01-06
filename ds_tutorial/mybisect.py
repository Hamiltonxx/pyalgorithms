import bisect 
lst = [1,3,4,4,4,6,7]

print("The rightmost index to insert, keeping list sorted: ")
print(bisect.bisect(lst,4))

print("The leftmost index to insert")
print(bisect.bisect_left(lst,4))

print("The rightmost index to insert, from 0 to 4:")
print(bisect.bisect_right(lst,4,0,4))

l1,l2,l3 = [1,3,4,4,4,6,7],[1,3,4,4,4,6,7],[1,3,4,4,4,6,7]

bisect.insort(l1,5)
print(l1)
bisect.insort_left(l2,5)
print(l2)
bisect.insort_right(l3,5,0,4)
print(l3)

print(bisect.bisect(lst,5))