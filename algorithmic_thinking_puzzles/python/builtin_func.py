# filter()
# filter(func, iterable) == (item for item in iterable if func(item))
func = lambda x: x in ['a', 'e', 'i', 'o', 'u']
print(list(filter(func, ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'])))
multiple_of_3 = lambda x: x % 3 == 0
print(list(filter(multiple_of_3, [1,2,3,4,5,6,7,8,9,10])))

# map()
symbols = '$¢£¥€¤'
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# 这里可以使用列表推导式，更易理解且速度更快
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]