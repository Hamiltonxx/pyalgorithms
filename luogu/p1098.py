# '-' 45
# '0'~'9' 48~57
# 'A'~'Z' 65~90
# 'a'~'z' 97~122

p1,p2,p3 = map(int,input().split())
s = list(input())

for i in range(1,len(s)-1):
    if s[i] == '-':
        if s[i-1]=='-' or s[i+1]=='-':
            continue
        if s[i-1].isdecimal() and s[i+1].isdecimal():
            l,r = int(s[i-1]),int(s[i+1])
            if r - l == 1:
                s[i] = ""
            if r - l > 1:
                if p1==3:
                    s[i] = '*'*p2*(r-l-1)
                else:
                    s[i]=""
                    for j in range(l+1,r):
                        s[i] += str(j)*p2
                    if p3==2: s[i] = s[i][::-1]
        if s[i-1].islower() and s[i+1].islower() or s[i-1].isupper() and s[i+1].isupper():
            l,r = ord(s[i-1]),ord(s[i+1])
            if r-l == 1:
                s[i] = ""
            if r-l > 1:
                if p1==3:
                    s[i] = '*'*p2*(r-l-1)
                else:
                    s[i] = ""
                    for j in range(l+1,r):
                        s[i] += chr(j)*p2
                    if p1==1:
                        s[i] = s[i].lower()
                    if p1==2:
                        s[i] = s[i].upper()
                    if p3==2:
                        s[i] = s[i][::-1]

print("".join(s))
