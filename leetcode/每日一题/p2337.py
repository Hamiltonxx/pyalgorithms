# def canChange(start, target):
#     sR, tL = 0, 0
#     for a,b in zip(start, target):
#         if a == 'R':
#             sR += 1
#         if b == 'L':
#             tL -= 1
#         if sR != 0 and tL != 0:
#             return False
#         if b == 'R':
#             sR -= 1
#             if sR < 0:
#                 return False
#         if a == 'L':
#             tL += 1
#             if tL > 0:
#                 return False
#     return sR == tL == 0

# def canChange(start, target):
#     if start.count('_') != target.count('_') or start.count('L') != target.count('L'):
#         return False
#     s = start.replace("_","")
#     t = target.replace("_","")
#     for x,y in zip(s,t):
#         if x!=y:
#             return False
#     return True 

def canChange(start, target):
    if start.count('_') != target.count('_'):
        return False
    s = [(ch,i) for i,ch in enumerate(start) if ch!='_']
    t = [(ch,i) for i,ch in enumerate(target) if ch!='_']
    for (sc,si),(tc,ti) in zip(s,t):
        if sc != tc: return False
        if sc == 'L' and si < ti: return False
        if sc == 'R' and si > ti: return False
    return True

start = "_L__R__R_"
target = "L______RR"
# start = "R_L_"
# target = "__LR"
print(canChange(start,target))