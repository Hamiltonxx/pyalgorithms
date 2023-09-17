from collections import deque
def minJump(forbidden, a, b, x):
    forbidden, lower, upper = set(forbidden), 0, max(x, max(forbidden)) + a + b
    q, steps = deque(), -1
    q.append((0,True))
    forbidden.add(0)

    while q:
        steps += 1
        for i in range(len(q)):
            pos, backable = q.popleft()
            if pos == x:
                return steps
            if backable and pos - b > 0 and pos-b not in forbidden:
                q.append((pos-b,False))
                forbidden.add(pos-b)
            if pos+a <= upper and pos+a not in forbidden:
                q.append((pos+a,True))
                forbidden.add(pos+a)
        
    return -1
