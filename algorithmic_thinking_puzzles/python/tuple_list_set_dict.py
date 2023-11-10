# set
st = set()
st.add('u')
st.add('v')
# st.remove('z') # raise error
st.discard('z')

x, y = {'a','b','c','d'}, {'c','d','e','f'}
print(x.difference(y))
print(x - y)
print(x.union(y))
print(x | y) # not x + y
print(x.intersection(y))
print(x & y)
print(x.symmetric_difference(y))
print(x ^ y)

print(x == y)
print(x != y)


print(x.isdisjoint(y))
z = x & y 
print(z.issubset(x))
print(z <= x)
print(z < x) # proper subset
print(y.issuperset(z))
print(y >= z)
print(y > z) # proper superset

x.update(y)
print(x)

# dict
d = {'k1':'v1','k2':'v2','k3':'v3'}
d = ([('k1','v1'),('k2','v2'),('k3','v3')])
d = dict(k1='v1',k2='v2',k3='v3')
print(d)
# The entries in the dictionary display in the order they were defined.
# But that is irrelevant when it comes to retrieving them.
# Dictionary elements are not accessed by numerical index.
d = {(1,1):'a',(1,2):'b'}
# d = {[1,1]:'a',[1,2]:'b'} # Wrong, lists and dicts are mutable
# hash(d) # Wrong, unhashable type 'list'
print('k1' in d)
print('k4' not in d)
print(len(d))
d.clear()
d.get('k5','default') # d.get('k5')
print(d.items())
print(d.keys())
print(d.values())
d.pop('k1') # {'k2':'v2','k3':'v3'}
d.pop('k6') # Raise KeyError
d.pop('k6', -1) # No Error
d.popitem() # Removes the last key-value pair, raise a KeyError if dict is empty.
d2 = {'k4':'v4','k5':'v5'}
d.update(d2)
d.update([('k6','v6'),('k7','v7')])

d.pop(next(iter(d))) # removes the first(leftmost) item
d.popitem() # removes the recent(rightmost) item