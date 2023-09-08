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