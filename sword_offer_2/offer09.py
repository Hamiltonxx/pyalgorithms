# stack0, stack1 = [], []

# def appendTail(value):
#     stack0.append(value)

# def deleteHead():
#     if not stack0:
#         return -1
#     while stack0:
#         stack1.append(stack0.pop())
#     res = stack1.pop()
#     while stack1:
#         stack0.append(stack1.pop())
#     return res

# appendTail(3)
# appendTail(2)
# print(deleteHead())
# print(deleteHead())
# print(deleteHead())

class CQueue:

    def __init__(self):
        self.stack0 = []
        self.stack1 = []

    def appendTail(self, value: int) -> None:
        self.stack0.append(value)

    def deleteHead(self) -> int:
        if not self.stack0:
            return -1
        while self.stack0:
            self.stack1.append(self.stack0.pop())
        res = self.stack1.pop()
        while self.stack1:
            self.stack0.append(self.stack1.pop())

obj = CQueue()
obj.appendTail(3)
param_2 = obj.deleteHead()
print(param_2)