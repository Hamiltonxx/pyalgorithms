N = int(input())

if N >= 401:
    ans = 150*0.4463 + 250*0.4663 + (N-400)*0.5663
elif N >= 151:
    ans = 150*0.4463 + (N-150)*0.4663
else:
    ans = N*0.4463

print(f"{ans:.1f}")