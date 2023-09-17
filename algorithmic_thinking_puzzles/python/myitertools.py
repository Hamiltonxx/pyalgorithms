# chain
# takes a series of iterables and returns one iterable.
from itertools import chain, accumulate
odd, even = [1,3,5], [2,4,6]
numbers = chain(odd, even)
print(list(numbers))
chars = chain('ABC','DEF','GHI','JKL')
print(list(chars))
print("chain a 2d array")
print(list(chain([odd,even])))
print("using *")
print(list(chain(*[odd,even])))
print("using from_iterable")
numbers2 = chain.from_iterable([odd,even])
print(list(numbers2))

li = ['123','456','789']
sm = sum(map(int,chain(*li)))
print(sm)

# accumulate
diff = [0, 10, 45, -10, -20, 0]
print(list(accumulate(diff)))