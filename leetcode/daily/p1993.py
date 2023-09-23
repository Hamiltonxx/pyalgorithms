class LockingTree:
    def __init__(self, parent):
        self.parent = parent 
        self.tree = [[] for _ in parent]
        for i,x in enumerate(parent):
            if x != -1: self.tree[x].append(i)
        self.locked = {}

    def lock(self, num, user):
        if num in self.locked: return False
        self.locked[num] = user
        return True
    
    def unlock(self, num, user):
        if self.locked.get(num) != user: return False
        self.locked.pop(num)
        return True
    
    def upgrade(self, num, user):
        if num in self.locked: return False
        node = num 
        while node != -1:
            if node in self.locked: break # locked ancestor
            node = self.parent[node]
        else:
            stack = [num]
            descendant = []
            while stack:
                node = stack.pop()
                if node in self.locked: descendant.append(node)
                for child in self.tree[node]: stack.append(child)
            if descendant:
                self.locked[num] = user
                for node in descendant: self.locked.pop(node) # unlock all descendant
                return True
        return False