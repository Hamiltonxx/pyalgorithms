# timeit has both a Command-Line Interface as well as a callable one.
# The Python library runs the code statement 1 million times and provides the minimum time 
# taken from the given set of code snippets.
# Command Line: python3 -m timeit '"-".join(str(n) for n in range(100))'

import timeit 
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)

# timing functions
def hasDigit(somelist):
    str_with_digit = []
    for string in somelist:
        check_char = [char.isdigit() for char in string]
        if any(check_char):
            str_with_digit.append(string)
    return str_with_digit