# def translateNum(num):
#     if len(num)==1:
#         return 1
#     if len(num)==2:
#         return 2 if num<"26" else 1
#     return translateNum(num[1:])+translateNum(num[2:])

def translateNum(num):
    if num<10:
        return 1
    if 9<num%100<26:
        return translateNum(num//10)+translateNum(num//100)
    return translateNum(num//10)

print(translateNum(12258))
