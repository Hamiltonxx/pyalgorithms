T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    Sa = Sb = 0
    for i in range(1000):
        Sa = Sa + (2*i+1)
        Sb = Sb + (2*i+2)
        if Sa > A:
            print("Bob")
            break 
        if Sb > B:
            print("Limak")
            break 
