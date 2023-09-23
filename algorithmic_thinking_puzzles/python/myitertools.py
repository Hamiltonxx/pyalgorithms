# chain
# takes a series of iterables and returns one iterable.
from itertools import chain, accumulate, compress, product, combinations, permutations
print(list(chain(*[[1,3,5],[2,4,6]])))
print(list(chain('ABC','DEF','GHI','JKL')))
li = ['123','456','789']
sm = sum(map(int,chain(*li)))
print(sm)

# product
print(list(product('ABCD','EF','GHI')))

# combinations
print(list(combinations('ABCD',2)))

# permutations
print(list(permutations('ABCD',2)))

# accumulate
diff = [0, 10, 45, -10, -20, 0]
print(list(accumulate(diff)))

# compress
print(list(compress('ABCDEF',[1,0,1,0,1,1])))