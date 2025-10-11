#1 to display 1 - 10 numbers
for i in range(1, 11, 1):
    print(i)

#2 to display even numbers between 1 to 20
for i in range(0,21,2):
    print(i)

#3 to dislay odd numbers between 1 to 20
for i in range(1,21,2):
    print(i)

#4 to display 10 to 1 numbers
for i in range(10, 0, -1):
    print(i)

#5 To display square of 1 to 10 numbers
for i in range(1, 11, 1):
    print("Square of number is :", i**2)

#6 To display cube of 1 to 10 numbers
for i in range(1, 11, 1):
    print("Square of number is :", i**3)

#7 to display square of even no and cube of odd numbers
for i in range(1, 21):
    if i % 2 == 0:
        print("Square of even numbers :", i**2)
    else:
        print("cube of odd numbers :", i**3)

#8 to calculate sum of 1 to 10 numbers
sum = 0
for i in range(1, 11):
    sum+=i
print(sum)

#9) to display factorial of given number
n = int(input("Enter the number to get factorial: "))
fact = 1

for i in range(1, n+1):
    fact *= i
print("factorial of number is: ", fact)

#10 to display square root of 1 to 10 numbers
import math

for i in range(1, 11):
    print(f"square root of {i} is", math.sqrt(i))


#11 to display multiplication table of given number
n = int(input("Enter a number to get multiplication table: "))
mul = 1

for i in range(1, 11):
    mul = n * i
    print(f"{n} x {i} = ", mul)