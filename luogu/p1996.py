n,m = map(int,input().split())
guy = list(range(n))

while guy:
    pos = (m-1) % len(guy)
    print(guy[pos]+1, end=" ")
    guy = guy[pos+1:] + guy[:pos]
