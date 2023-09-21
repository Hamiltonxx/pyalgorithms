import bisect 
lst = [1,3,4,4,4,6,7]

print("The rightmost index to insert")
print(bisect.bisect(lst,4))

print("The leftmost index to insert")
print(bisect.bisect_left(lst,4))

print("The rightmost index to insert, from 0 to 4:")
print(bisect.bisect_right(lst,4,0,4))

l1,l2,l3 = [1,3,4,4,4,6,7],[1,3,4,4,4,6,7],[1,3,4,4,4,6,7]

bisect.insort(l1,5)
print(l1)
bisect.insort_left(l2,5)
print(l2)
bisect.insort_right(l3,5,0,4)
print(l3)

print(bisect.bisect(lst,5))

from collections import namedtuple
from pprint import pprint
Movie = namedtuple('Movie', ('name', 'released', 'director'))
movies = [
    Movie('Jaws', 1975, 'Spielberg'),
    Movie('Titanic', 1997, 'Cameron'),
    Movie('The Birds', 1963, 'Hitchcock'),
    Movie('Aliens', 1986, 'Cameron')
]
byrelease = lambda x:x.released
movies.sort(key=byrelease)
print(movies)
print(bisect.bisect(movies, 1970, key=byrelease))
romance = Movie('Love Story', 1970, 'Hiller')
bisect.insort(movies, romance, key=byrelease)
pprint(movies)