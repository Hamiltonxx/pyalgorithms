''' sys.stdin.readline() is 4 times faster than input() '''

n,k = map(int, input().split())

cnt = 0
for _ in range(n):
    x = int(input())
    if x % k == 0:
        cnt += 1

print(cnt)


# from sys import stdin 

# n,k = map(int, stdin.readline().split())

# cnt = 0
# for _ in range(n):
#     x = int(stdin.readline())
#     if x % k == 0:
#         cnt += 1

# print(cnt) 

