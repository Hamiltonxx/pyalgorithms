s = input()

if "." in s:
    a,b = s.split(".")
    rb = b[::-1]
    for i in range(len(rb)-1,-1,-1):
        if rb[i] != "0":
            break 
    rb = rb[:i+1]
    print(f"{int(a[::-1])}.{rb}")
elif "/" in s:
    a,b = s.split("/")
    print(f"{int(a[::-1])}/{int(b[::-1])}")
elif "%" in s:
    a = s[:-1]
    print(f"{int(a[::-1])}%")
else:
    print(int(s[::-1]))