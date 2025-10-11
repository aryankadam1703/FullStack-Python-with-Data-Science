#1 to display square root of 1 to 10 numbers
import math

for i in range(1, 11):
    print(f"square root of {i} is", math.sqrt(i))


#2 to display multiplication table of given number
n = int(input("Enter a number to get multiplication table: "))
mul = 1

for i in range(1, 11):
    mul = n * i
    print(f"{n} x {i} = ", mul)