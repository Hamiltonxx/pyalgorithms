t = int(input())
for i in range(t):
    line = input()
    lst = []
    longest = cur_len = 0
    for x in line:
        if x=='>':
            if lst == []:
                continue
            else:
                lst.pop()
                cur_len += 2
                if longest < cur_len:
                    longest = cur_len
                if lst == []:
                    cur_len = 0
        else:
            lst.append('<')
    print(longest)



