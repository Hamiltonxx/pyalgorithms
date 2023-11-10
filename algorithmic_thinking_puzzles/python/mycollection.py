from collections import OrderedDict
# OrderedDict
# OrderedDict has become less important now that the built-in dict class gained the ability to remember insertion order.
# The OrderedDict algorithm can handle frequent reordering operations better than dict.
d = {}
od = OrderedDict.fromkeys('abcde')
# pop
od.popitem(last=True)
d.popitem()
od.popitem(last=False)
k = next(iter(d))
d.pop(k)

# move to end
od.move_to_end(k, last=True)
d[k] = d.pop(k)

