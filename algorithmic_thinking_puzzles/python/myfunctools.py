# Higher-orderr functions
# When either a function takes another function as an input or returns another function as output,
# then such functions are called higher-order functions.
# map(), reduce() and filter() are all higher-order functions
def create_function(aggregation: str):
    if aggregation == "sum":
        return sum
    elif aggregation == "mean":
        def mean(arr: list):
            return sum(arr)/len(arr)
        return mean
    return None
# The most commonly used functions from this module:
# functools.reduce, functools.partial, functools.cache, functools.lru_cache, functools.wraps

# functools.reduce() takes two arguments, a function and an iterable.
# The input function is applied on the next iterable element with the result from the last run, which results a cumulative output.
from functools import reduce
# print(reduce(lambda x,y: x*y, [1,2,3,4])) # 24
# def multiply(lst):
#     return reduce(lambda x,y: x*y, lst)
mul = lambda lst:reduce(lambda x,y: x*y, lst)
print(mul([1,2,3,4]))

# functools.partial()
# functools.cache
from functools import cache 
@cache 
def fibonacci(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4)) # called 5 times
print(fibonacci(11)) # called 7 times
# The cache size is unbounded and therefore the cached dictionary can grow to enormous sizes.

# A better alternative to @cache is @lru_cache
from functools import lru_cache 
@lru_cache(maxsize=2)
def fibonacci(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4)) # called 8 times
print(fibonacci(11)) # called 81 times

# functools.wraps
# When a decorator is used on a function, the function loses information about itself.