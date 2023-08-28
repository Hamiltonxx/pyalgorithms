from functools import lru_cache

# @lru_cache(None)
# def canMakeSubsequence(str1, str2):
#     if not str2:
#         return True
#     if not str1:
#         return False
#     a,b = ord(str1[0]), ord(str2[0])
#     if a==b or a+1==b or a-b==25:
#         return canMakeSubsequence(str1[1:],str2[1:])
#     else:
#         return canMakeSubsequence(str1[1:],str2)

def canMakeSubsequence(str1, str2):
    start = 0
    # n = len(str1)
    # for x in str2:
    #     for i in range(n):
    #         if str1[i]==x or ord(str1[i])+1==ord(x) or (str1[i]=='z' and x=='a'):
    while str1 and str2:
        if str1[0]==str2[0] or ord(str1[0])+1==ord(str2[0]) or (str1[0]=='z' and str2[0]=='a'):
            str1, str2 = str1[1:], str2[1:]
        else:
            str1 = str1[1:]
    if str2:
        return False
    else:
        return True
    
def can_make_sub(str1, str2):
    

    
str1 = "zc"
str2 = "ad"
print(canMakeSubsequence(str1,str2))
