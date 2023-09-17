from itertools import product
def letterComb(digits):
    cs = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    p = product(*[cs[x] for x in digits])
    return [''.join(x) for x in p]