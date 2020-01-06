
from itertools import permutations 
permN = permutations([1,2,3])
print(list(permN))
print("### permutations of Length M ###")
permM = permutations([1,2,3],2)
print(list(permM))

from itertools import combinations 
print("### combinations of Length M ###")
comb = combinations([1,2,3],2)
print(list(comb))

from itertools import combinations_with_replacement 
print("### combinations_with_replacement of Length M, ###")
combrp = combinations_with_replacement(range(1,5),2)
print(list(combrp))