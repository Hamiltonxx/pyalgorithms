dict = {'a':[1,2,3,4,5],'b':2}
x = dict['a']
# x = [0,0,0]
for i in range(5):
    x[i] = 0
print(dict)

y = dict['b']
y = y+3
print(dict)

# Python赋值过程中不明确区分拷贝和引用，一般对静态变量为拷贝，对动态变量为引用。
# (静态变量首次传递时也是引用，当需要修改静态变量时，因为静态变量不能改变，所以会生成新的空间存储数据)
# 字符串、数值、元组为静态变量；列表、字典为动态变量
# 如果是引用，则id(变量) 相同