# sort multiple keys
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people.sort(key=lambda x:(x[1],x[0]))
print(people)

# sorted dict
d = {'b':2,'a':1,'c':3}
sd = dict(sorted(d.items()))