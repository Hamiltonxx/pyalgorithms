n = int(input())
co = map(int, input().split())
ans = ""
for i,c in enumerate(co):
    if c==0:
        continue
    elif c>0:
        if i==0 and c==1:
            ans += "x^"+str(n-i)
        elif i==0 and c!=1:
            ans += str(c)+"x^"+str(n-i)
        elif i<n-1 and c==1:
            ans += "+"+"x^"+str(n-i)
        elif i<n-1 and c!=1:
            ans += "+"+str(c)+"x^"+str(n-i)
        elif i==n-1 and c==1:
            ans += "+"+"x"
        elif i==n-1 and c!=1:
            ans += "+"+str(c)+"x"
        else:
            ans += "+"+str(c)
    else:
        if i<n-1 and c==-1:
            ans += "-"+"x^"+str(n-i)
        elif i<n-1 and c!=-1:
            ans += str(c)+"x^"+str(n-i)
        elif i==n-1:
            ans += str(c)+"x"
        else:
            ans += str(c)


print(ans)

