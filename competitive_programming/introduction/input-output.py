from sys import stdin 
from random import randint 

def readint():
    return int(stdin.readline())

def readmatrix(n):
    M = []
    for _ in range(n):
        row = list(map(int, stdin.read().split()))
        assert len(row) == n 
        M.append(row)
    return M 

def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]

def freivalds(n, A, B, C):
    x = [randint(0,1000000) for j in range(n)]
    return mult(A, mult(B,x)) == mult(C, x)

if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(n,A,B,C))