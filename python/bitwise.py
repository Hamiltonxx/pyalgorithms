a = 60 # 0b 11 1100
b = 13 # 0b    1101
print(f"a={a}, {bin(a)}; b={b}, {bin(b)}")

# binary AND
c = a & b 
print(c,bin(c))
# binary OR
c = a | b 
print(c, bin(c))
# binary XOR
c = a ^ b 
print(c, bin(c))
# binary Complement
c = ~a
print(c, bin(c))
# left shift
c = a << 2
print(c, bin(c))
# right shift
c = a >> 2
print(c, bin(c))

print(int(0b01000001))