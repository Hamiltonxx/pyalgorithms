# import sys 

# for line in sys.stdin:
#     arr = list(map(int, line.split()))
#     if len(arr) == 1:
#         n = arr[0]
#         if n == 0:
#             exit()
#     else:
#         avg = sum(arr) // n
#         res = sum([x-avg for x in arr if x>avg])
#         print(res)
#         print()

# arr = [4,4,4,4,4,4]
# avg = sum(arr) // 6
# res = sum([x-avg for x in arr if x>avg])
# print(res)

while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    avg = sum(arr) // n
    res = sum([x-avg for x in arr if x>avg])
    print(f'{res}\n')
