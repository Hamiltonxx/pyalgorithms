def translate2b(string):
    res = ""
    for x in string:
        if x=="d" or x=="f": res += "1"
        else: res += "0"
    return res 

T = int(input())
for _ in range(T):
    n = int(input())
    t = 0
    m = {}
    for __ in range(n):
        line = input()
        if line in m:
            t += m[line] // 2 
        else:
            s = translate2b(line)
            t2 = 2 + sum([4-(int(p)^int(q))*2 for (p,q) in zip(s,s[1:])])
            m[line] = t2 
            t += t2 
    print(t)
