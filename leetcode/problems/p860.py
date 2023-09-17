# from collections import Counter
# def lemonadeChange(bills):
#     ctr = Counter(bills)
#     if ctr[10] > ctr[5]:
#         return False 
#     if ctr[20] > ctr[5] - ctr[10]:
#         return False
#     if ctr[10]*10 + (ctr[5]-ctr[10])*5 < ctr[20]*15:
#         return False
#     return True 

def lemonadeChange(bills):
    n5 = n10 = 0
    for b in bills:
        if b==5: 
            n5 += 1
        elif b==10:
            n10 += 1
            n5 -= 1
            if n5 < 0: return False
        else:
            if n10:
                n10 -= 1
                n5 -= 1
            else:
                n5 -= 3
            if n5 < 0:
                return False
    return True
            
        