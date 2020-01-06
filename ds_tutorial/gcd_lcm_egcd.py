import math 

print(math.gcd(36,60))  #12

print(36 * 60 // math.gcd(36,60)) #180.0

# Extended Eculidean Algorithm
def egcd(a,b):
    if a==0: return (b,0,1)
    else:
        g,x,y = egcd(b%a, a)
        return (g,y-b//a*x,x)

# g,x,y = egcd(30,50)
# print(egcd(36,60))