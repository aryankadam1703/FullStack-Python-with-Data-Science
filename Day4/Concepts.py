#Agenda - Operators
#Arithmetic Operators(**, //)
# // - Floor division operator
# Comparison Operators (==, !=, >, <, >=, <=)
# Logical Operators (and, or, not)
# Membership Operators (in, not in)
# Identity Operators (is, is not)

# ** - Exponentiation operator
a = 2
ans = a**3
print("Exponentiation:", ans)

#// (floor division) - used to divide and round down to the nearest whole number
a = 2
b = 5
ans1 = b / a
ans2 = b // a
print("Division:", ans1)
print("Floor Division (rounded down):", ans2)

#Comparison Operators
a = 5

a == 5  # True
a != 5  # False
a != 10  # True
a > 3  # True
a >= 6  # False
a < 10  # True
a <= 50  # True

#Logical Operators 
# And - True if both operands are true
# Or - True if at least one operand is true
# not - True if the operand is false
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True

#Bitwise Operators
# Bitwise AND, OR, XOR, NOT, left shift, right shift
#          &   |    ^    ~       <<          >>

#numbers are converted to binary for bitwise operations, performs bitwise operation and then converted back to decimal
a = 7
b = 5

print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)
print(~b)  # Bitwise NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift
