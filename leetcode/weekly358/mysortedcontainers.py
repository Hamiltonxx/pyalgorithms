# At the core of Sorted Containers is the mutable sequence data type SortedList.
# The SortedList maintains its values in ascending sort order.
# As with built-in list datatype, SortedList supports duplicate elements and fast random-access indexing.
from sortedcontainers import SortedList
sl = SortedList()
# Values may be added to a SortedList using either SortedList.update() or SortedList.add().
sl.update([5,1,3,4,2])
print(sl)
sl.add(0)
print(sl)
# Remove elements by value: SortedList.discard() and SortedList.remove()
# Remove elements by index: SortedList.pop() and SortedList.__delitem__()
# Remove all: SortedList.clear()
sl.remove(0)
print(sl)
sl.discard(1)
print(sl)
sl.pop()
print(sl)
del sl[1]
print(sl)
sl.clear()
print(sl)
# Because SortedList is sorted, it supports efficient lookups by value or by index.
# Values can be found in logarithmic time.
# SortedList.__contains__(), SortedList.count(), SortedList.index(), 
# SortedList.bisect_left(), SortedList.bisect_right(), SortedList.__getitem__()
sl = SortedList('abbcccddddeeeee')
print('f' in sl)
print(sl.count('e'))
print(sl.index('c'))
print(sl[3])
print(sl.bisect_left('d'))
print(sl.bisect_right('d'))
print(sl[6:10])
# Iterate
# SortedList.__iter__(), SortedList.__reversed__(),
# SortedList.irange(), SortedList.islice()
sl = SortedList('acegi')
print(list(iter(sl)))
print(list(reversed(sl)))
print(list(sl.irange('b','h')))
print(list(sl.islice(1,4)))
# SortedList.__add__(), SortedList.__mul__()
print(sl+sl)
print(sl*3)

# SortedDict keys are maintained in sorted order.
from sortedcontainers import SortedDict 
sd = SortedDict()
# add item
# SortedDict.__setitem__(), SortedDict.update(), SortedDict.setdefault()
sd['e'] = 5
sd['b'] = 2
print(sd)
sd.update({"d":4,"c":3})
print(sd)
sd.setdefault('a',1)
print(sd)
# remove item
# SortedDict.__delitem__(), SortedDict.pop(), SortedDict.popitem()
del sd['d']
print(sd)
print(sd.pop('c'))
print(sd.popitem(index=-1))
print(sd)
# Look up keys
# SortedDict.__getitem__(), SortedDict.__contains__(), SortedDict.get(), SortedDict.peekitem()
print(sd['b'])
print('c' in sd)
print(sd.get('z') is None)
print(sd.peekitem(index=-1))

print(sd.bisect_right('b'))
print(sd.index('a'))
print(list(sd.irange('a','z')))

print(sd.keys(), sd.items(), sd.values())

# SortedSet.
from sortedcontainers import SortedSet
ss = SortedSet()
# SortedSet.__contains__(), SortedSet.add(), SortedSet.update(), SortedSet.discard()
ss.add('b')
ss.add('c')
ss.add('a')
ss.add('b')
print(ss)
print('c' in ss)
ss.discard('a')
ss.remove('b')
what = ss.update('def')
print(what)
ss.discard('z') # remove('z')会抛异常
print(ss)
# SortedSet.__getitem__(), SortedSet.__reversed__(), SortedSet.__delitem__(), SortedSet.pop()
print(ss[0])
print(list(reversed(ss)))
del ss[0]
ss.pop(index=-1)
print(ss)
# SortedSet.difference(), SortedSet.intersection(), 
# SortedSet.symmetric_difference(), SortedSet.union()
abcd = SortedSet('abcd')
cdef = SortedSet('cdef')
print(abcd.difference(cdef))
print(abcd.symmetric_difference(cdef))
print(abcd.union(cdef))
print(abcd | cdef)
abcd |= cdef
print(abcd)
# SortedSet.bisect(), SortedSet.index(), SortedSet.irange(), SortedSet.islice()
ss = SortedSet('abcdef')
print(ss.bisect('d'))
print(ss.index('f'))
print(list(ss.irange('b','e')))
print(list(ss.islice(-3)))

