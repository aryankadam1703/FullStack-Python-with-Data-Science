#Agenda
#1. Membership Operators
#2. Identity Operators
#3. Assignment Operators
#4. Control Flow Statements
    #a. Conditional Statements
    #b. Iterative Statements
    #c. branching Statements


#1) Membership Operators(in, not in)
# Used to check if a value is present in a sequence (like lists, tuples, strings, set)
# in - True if value is found in the sequence
# not in - True if value is not found in the sequence 


#example with a list
a = ['Apple', 'Banana', 'Cherry', 'Orange']
print("Apple" in a) # True
print("apple" in a) # False
print("Grapes" not in a) # True
print("Apple" not in a) # False

#2. Identity Operators(is, is not)
# Used to check if two variables point to the same object in memory
# is - True if both variables point to the same object
# is not - True if both variables do not point to the same object

x = ["apple", "banana", 'cherry']
y = ["apple", "banana", 'cherry']
z = x

print(id(x), id(y), id(z))  # Different IDs for x and y, same ID for x and z
print(x is z) # True, x and z point to the same object
print(x is y) # False, x and y point to different objects
print(y is not x) # True, y and x are not the same object
print(x is not y) # True, x and y are not the same object
print(x is not z) # False, x and z point to the same object

#3. Assignment Operators(=, +=, -=, *=, /=, %=, //=, **=)
# Used to assign values to variables

a = 10
a -= 3  # Equivalent to a = a - 3
a *= 2  # Equivalent to a = a * 2
a /= 4  # Equivalent to a = a / 4
a %= 3  # Equivalent to a = a % 3
a //=2  # Equivalent to a = a // 2


#4. Control Flow Statements
# a. Conditional Statements (if, elif, else)