line = input()
s = line[0]+line[2:5]+line[6:11]

num = 0
for i in range(9):
    num += int(s[i]) * (i+1)

res = num % 11
if res==10:
    res="X"
if str(res)==line[-1]:
    print("Right")
else:
    print(line[:-1]+str(res))
