# All string methods return new string.
print("hello world".capitalize())
print("abc".center(9))
print("abc".center(10,"0"))
print("abc".ljust(10,"0"))
print("abc".rjust(10,"0"))
print("   abc  ".lstrip())
print("   abc  ".rstrip())
print("   abc  ".strip())
print("hello world".replace("o","#",1))
print("hello world 233".split())
print("hello world 233".split(" ",1))
print("hello world 233".rsplit(" ",1))
print("thank you\nyou're welcome".splitlines())
print("Hello world".upper())
print("Hello world".lower())
print("Hello world".swapcase())

print("hello world".count("o"))
print("hello world".count("o",6,11))
print("hello world".startswith("he"))
print("hello world".endswith("rld"))
print("hello world".endswith("rld",6,11))
print("hello world".find("wor"))
print("hello world".find("wor",6,11))
print("hello world".find("xor"))
print("hello world".index("wor")) # raise exception if not found
print("hello world".rfind("o"))
print("hello world".rindex("o"))

print("Hello world 233".isalnum()) # (space)!#%&? not alnum
print("Helloworld233".isalnum()) # (space)!#%&? not alnum
print("Helloworld".isalpha()) # (space)!#%&? not alpha
print("#Hello world 233".isascii())
print("\u0033".isdecimal()) # unicode for 3
print("0344".isdecimal())
print("\u00B2".isdigit())
print("Demo002".isidentifier()) # a-z,0-9,_
print("2bring".isidentifier()) # ^number,space
print("hello world 123".islower())
print("65535".isnumeric())
print("1.5".isnumeric()) # "-1","1.5"
print("   ".isspace())
print("Hello world".isupper())

print("#".join(("John","Peter","Lisa")))

