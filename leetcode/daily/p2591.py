# def distMoney(money, children):
#     if money < children: return -1
#     quo, rem = divmod(money, 8)
#     if rem == 4:
#         # 20/28 2
#         if quo >= children:
#             return children - 1
#         else: # 12 2 # 4 2
#             return quo-1 if quo>=1 else 0
#     else: # 8 2 # 16 3
#         # 19 3  #27 3
#         return min(quo, children)

def distMoney(money, children):
    if money < children: return -1
    if money == 8*children: return children
    if money > 8*children: return children-1
    money -= children # 每人一块
    if money < 7: return 0
    quo, rem = divmod(money, 7)
    if rem == 3 and children==quo+1:
        quo -= 1
    return quo
        


    