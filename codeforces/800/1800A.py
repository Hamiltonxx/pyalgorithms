t = int(input())
for _ in range(t):
    n = int(input())
    s = input().lower()
    pm=pe=po=pw=p=0
    if s[0] != "m":
        print("NO")
    else:
        for i in range(1,n):
            if s[i]=="m":
                pass 
            elif s[i]=="e":
                p = i
            else:
                print("NO")
    # for i in range(n-1):
    #     if s[i] in "meow" and s[i+1] in "meow":
    #         pass 
    #     else:
    #         break
    # pm=pe=po=pw=i=0
    # for c in s:
        # if c not in "meow":
        #     print("NO")
        #     break
    #     if c=="m" and pm==0:
    #         pm = i 
    #     elif c=="e" and pe==0:
    #         pe = i
    #     elif c=="o" and po==0:
    #         po = i 
    #     elif c=="w" and pw==0:
    #         pw = i 
    #     i += 1
    # if not pm<pe<po<pw:
    #     print("NO")
    #     continue

    



