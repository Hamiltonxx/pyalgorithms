from collections import defaultdict, deque
def canVisitAllRooms(rooms):
    visited = set()
    q = deque([0])
    while q:
        v = q.popleft()
        if v not in visited:
            visited.add(v)
            for u in rooms[v]:
                if u not in visited:
                    q.append(u)
    return len(visited) == len(rooms)

rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms))
