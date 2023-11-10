# import sys 

# for line in sys.stdin:
#     try:
#         N = int(line)
#         d = {}
#         mg,yu = 1,2
#         seen = set()
#     except:
#         if N:
#             a,b = map(int, input().split())
#             d[a] = b
#         else:
#             while True:
#                 if mg == yu:
#                     print('You are my brother')
#                     break
#                 elif mg in seen or yu not in d:
#                     print('You are my elder')
#                     break
#                 elif yu in seen or mg not in d:
#                     print('You are my younger')
#                     break
#                 else:
#                     seen.add(mg)
#                     seen.add(yu)
#                     mg = d[mg]
#                     yu = d[yu]
#         N -= 1




while True:
    try:
        N = int(input())
        d = {}
        for _ in range(N):
            a,b = map(int, input().split())
            d[a] = b
        mg,yu = 1,2
        seen = set()
        while True:
            if mg == yu:
                print('You are my brother')
                break
            elif mg in seen or yu not in d:
                print('You are my elder')
                break
            elif yu in seen or mg not in d:
                print('You are my younger')
                break
            else:
                seen.add(mg)
                seen.add(yu)
                mg = d[mg]
                yu = d[yu]
    except:
        break

