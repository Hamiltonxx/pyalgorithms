def convert(s, rs):
    if rs == 1:
        return s
    ta = [""] * rs
    idx = 0
    inc = 1
    for x in s:
        ta[idx] += x
        if idx == 0:
            inc = 1
        elif idx == rs-1:
            inc = -1
        idx += inc
    return "".join(ta)