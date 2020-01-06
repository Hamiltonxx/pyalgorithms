# def factorial(n):
#     if n==1: return 1
#     return n * factorial(n-1)

# print(factorial(4))

def factorial(n):
    print(f"factorial has been called with n = {n}")
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print(f"intermediate result for {n} * factorial({n-1}) is {res}")
        return res  

print(factorial(5))

def fib(n):
    if n==0: return 0
    elif n==1: return 1
    else: return fib(n-1)+fib(n-2)

print(fib(5))
