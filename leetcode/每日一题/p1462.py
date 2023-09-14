from collections import defaultdict
def checkIfPrerequisite(numCourses, prerequisites, queries):
    descendant, ancestor = defaultdict(set), defaultdict(set)
    for u,v in prerequisites:
        descendant[u].add(v)
        ancestor[v].add(u)
        for x in ancestor[u]:
            descendant[x].add(v)
        ancestor[v] |= ancestor[u]
        descendant[u] |= descendant[v]
    
    return [v in descendant[u] for u,v in queries]

print(checkIfPrerequisite(4, [[2,3],[2,1],[0,3],[0,1]], [[0,1]]))
     


    
    