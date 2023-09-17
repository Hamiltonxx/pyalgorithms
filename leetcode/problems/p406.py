def reconstructQueue(people):
    people.sort(key=lambda x:(-x[0],x[1]))
    ans = []
    for p in people:
        ans.insert(p[1], p)
    return ans


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))