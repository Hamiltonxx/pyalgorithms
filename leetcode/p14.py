strs = ["flower","flow","flight"]

# cmm = ""
# for x in zip(*strs):
#     s = set(x)
#     print(s[0])

import os 
print(os.path.commonprefix(strs))
