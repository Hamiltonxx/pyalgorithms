line = input()
stack = []
s=""
res=0
for x in line:
    if x=="@":
        break 
    if x.isdigit():
        s+=x 
    if x==".":
        stack.append(int(s))
        s=""
    if x=="+":
        res = stack.pop() + stack.pop()
        stack.append(res)
    if x=="-":
        a,b = stack.pop(),stack.pop()
        res = b-a
        stack.append(res)
    if x=="*":
        res = stack.pop() * stack.pop()
        stack.append(res)
    if x=="/":
        a,b = stack.pop(),stack.pop()
        res = b//a
        stack.append(res)
print(res)