def valid_length(str):
    l = 0
    opening_brackets = 0
    for i,ch in enumerate(str):
        if ch == '>':
            if opening_brackets == 0:
                return l
            opening_brackets -= 1
        else:
            opening_brackets += 1

        if opening_brackets == 0:
            l = i + 1
    return l

T = int(input())

for i in range(T):
    str = input()
    print(valid_length(str))