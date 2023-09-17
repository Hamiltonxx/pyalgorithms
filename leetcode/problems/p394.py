s = "mn3[a2[c12[bd]]e]xyz4[u]v"
# def decodeString(s):
#     num, res = '', 0
#     st = []
#     for ch in s:
#         if ch.isnumeric():
#             num = num*10 + int(ch)
#         elif ch == '[':
#             st.append(res)
#             st.append(num)
#             res, num = '', 0
#         elif ch == ']':
#             cnt = st.pop()
#             prev = st.pop()
#             res = prev + res * cnt
#         else:
#             res += ch
#     return res

# print(decodeString(s))

def decodeString(s):
    res, num = '', 0
    stack = []
    for c in s:
        if c.isnumeric():
            num = num * 10 + int(c)
        elif c == '[':
            stack.append((res,num))
            res, num = '', 0
        elif c == ']':
            prev, cnt = stack.pop()
            res = prev + res * cnt
        else:
            res += c
    return res 

print(decodeString(s))