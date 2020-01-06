#namedtuples
#deque
#ChainMap
#Counter
#OrderedDict
#defaultdict

# dq[1]=z is OK, when dq[1:2] error.
# The major advantage of deques over lists is that inserting
# items at the beginning of a deque is much faster than inserting
# items at the beginning of a list, although inserting items at the 
# end of a deque is very slightly slower than the equivalent operation
# on a list.
from collections import deque

dq = deque('abc')
dq.append('d')
dq.appendleft('z')
dq.extend('efg')
dq.extendleft('yxw')
print(dq)
# deque(['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(dq.pop())
print(dq.popleft())
print(dq)
# g
# w
# deque(['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'])

dq.rotate(2)
print(dq)
dq.rotate(-2)
print(dq)
# deque(['e', 'f', 'x', 'y', 'z', 'a', 'b', 'c', 'd'])
# deque(['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'])

dq = deque({1,2,3,4})
dq.append(5)
first = dq.popleft()

#ChainMap
# The advantage of using ChainMap objects, rather than just a dictionary,
# is that we retain previouly set values. 
from collections import ChainMap 
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5}
chainmap = ChainMap(dict1,dict2) #linking two dictionaries
print(chainmap)
print(chainmap.maps)
# print(chainmap.values)
# ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5})
# [{'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}]
print(chainmap['b'])
print(chainmap['e'])
# 2
# 5
dict3 = {'a':10,'f':7}
chainmap2 = ChainMap(dict1,dict2,dict3)
print(chainmap2.maps)
print(chainmap2['a'])
print(chainmap2.maps[2]['a'])
# [{'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}, {'a': 10, 'f': 7}]
# 1
# 10

# Counter 
# We can pass it any sequence object, a dictionary of key:value pairs, or a 
# tuple of the format (object=value,...)
# The most notable difference between counter and dictionaries is that counter
# return a zero count for missing items rather than raising a key error.
from collections import Counter 
print(Counter("anysequence"))
c2 = Counter({'a':1,'c':2,'e':3})
c3 = Counter(a=1,c=2,e=3)
print(c2)
print(c3)
# Counter({'e': 3, 'n': 2, 'a': 1, 'y': 1, 's': 1, 'q': 1, 'u': 1, 'c': 1})
# Counter({'e': 3, 'c': 2, 'a': 1})
# Counter({'e': 3, 'c': 2, 'a': 1})

c0 = Counter("hello world i am hamilton")
print(c0)
print(c0.most_common())
# Counter({'l': 4, ' ': 4, 'o': 3, 'h': 2, 'i': 2, 'a': 2, 'm': 2, 'e': 1, 'w': 1, 'r': 1, 'd': 1, 't': 1, 'n': 1})
# [('l', 4), (' ', 4), ('o', 3), ('h', 2), ('i', 2), ('a', 2), ('m', 2), ('e', 1), ('w', 1), ('r', 1), ('d', 1), ('t', 1), ('n', 1)]

# OrderedDict, remembers the insertion order 
# OrderedDict is often used in conjunction with the sorted method to create a sorted dictionary. 
from collections import OrderedDict
od1 = OrderedDict()
od1['one'] = 1
od1['two'] = 2
od2 = OrderedDict()
od2['two'] = 2
od2['one'] = 1
print(od1)
print(od2)
print(od1 == od2)
# OrderedDict([('one', 1), ('two', 2)])
# OrderedDict([('two', 2), ('one', 1)])
# False
kvs = [('three',3),('four',4),('five',5)]
od1.update(kvs)
print(od1)
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)])

od3 = OrderedDict(sorted(od1.items(), key=lambda t: (4*t[1]-t[1]**2)))
print(od3)
print(od3.values())
# OrderedDict([('five', 5), ('four', 4), ('one', 1), ('three', 3), ('two', 2)])
# odict_values([5, 4, 1, 3, 2])

# defaultdict, is a subclass of dict, and therefore they share methods and operations.
from collections import defaultdict
dd = defaultdict(int)
words = "red blue green red yellow blue red green green red".split()
for word in words:
    dd[word] += 1
print(dd)
print(Counter(words)["green"])
print(dd["green"])

## namedtuple
bob = ('Bob', 30, 'male')
print(bob)
jane = ('Jane', 29, 'female')
print("Field by index:",jane[0])
print("Fields by index:")
for p in [bob,jane]:
    print("{} is a {} year old {}".format(*p))
# ('Bob', 30, 'male')
# Field by index: Jane
# Fields by index:
# Bob is a 30 year old male
# Jane is a 29 year old female

# This makes tuples convenient containers for simple uses.
# In contrast, remembering which index should be used for each value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names, as well as the numerical index, to each member.
from collections import namedtuple
Person = namedtuple('Person','name age')
bob = Person(name='bob',age=30)
print(bob)
jane = Person(name='Jane',age=29)
print(jane.name)
print("Fields by index:")
for p in [bob,jane]:
    print('{} is {} years old'.format(*p))
# Person(name='bob', age=30)
# Jane
# Fields by index:
# bob is 30 years old
# Jane is 29 years old

