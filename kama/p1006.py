import sys 

d = {'A':4,'B':3,'C':2,'D':1,'F':0}
for line in sys.stdin:
    try:
        arr = [d[x] for x in line.split()]
        print(f'{sum(arr)/len(arr):.2f}')
    except:
        print('Unknown')