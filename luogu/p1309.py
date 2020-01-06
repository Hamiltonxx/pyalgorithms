N,R,Q = map(int,input().split())
s = list(map(int,input().split()))
w = list(map(int,input().split()))

S=[]
for i,x in enumerate(s):
    S.append([x,i,w[i]])
S.sort(key=lambda z:(-z[0],z[1]))

# for j in range(R):
#     for i in range(0,2*N-1,2):
#         if S[i][2]<S[i+1][2]:
#             S[i+1][0] += 1
#         else:
#             S[i][0] += 1
#     S.sort(key=lambda z:(-z[0],z[1]))

# print(S[Q-1][1]+1)

# for j in range(R):
#     if S[0][2]<S[1][2]:
#         S[1][0] += 1
#         if S[1][0]>S[0][0] or S[1][0]==S[0][0] and S[1][1]<S[0][1]:
#             S[0],S[1] = S[1],S[0]
#     else:
#         S[0][0] += 1

#     for i in range(1,N):
#         if S[2*i][2]>S[2*i+1][2]:
#             S[2*i][0] += 1
#             if S[2*i][0]>S[2*i-1][0] or S[2*i][0]==S[2*i-1][0] and S[2*i][1]<S[2*i-1][1]:
#                 S[2*i],S[2*i-1] = S[2*i-1],S[2*i]
#         else:
#             S[2*i+1][0] += 1
#             if S[2*i+1][0]>S[2*i][0] or S[2*i+1][0]==S[2*i][0] and S[2*i+1][1]<S[2*i][1]:
#                 S[2*i],S[2*i+1] = S[2*i+1],S[2*i]

# print(S[Q-1][1]+1)

for i in range(N-1)
