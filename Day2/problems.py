#Perform addition of two numbers

a = 20
b = 2

c = a + b
print("Addition of two numbers:", c)

d = a - b
print("Subtraction of two numbers:", d)

e = a * b
print("Multiplication of two numbers:", e)

f = a / b
print("Division pf two numbers:", f)

g = a % b
print("Modulus of two numbers:", g)


#2) Area of rectangle
Len = 5
Breadth = 5
Area = Len * Breadth
print("Area of Rectangle :", Area)

#3) Calculate area of square
side = 5
Area = side * side
print("Area of Square :", Area)

#4) Calculate area of cube
side = 5
Area = 6*side * side
print("Area of Cube :", Area)

#5)Calculate area of circle
r = 2
Area = 3.14 * r * r
print("Area of Cirlce :", Area)

#6) Calculate Simple Interest
p = 4000
n = 5
r = 8
interest = (p * n * r) / 100
print("Simple Interest :", interest)

#7) To accept 5 subject marks and calculate total and percentage
english = int(input("Enter marks for English: "))
maths = int(input("Enter Marks for Maths: "))
science = int(input("Enter Marks for Science: "))
social = int(input("Enter Marks for Social: "))
hindi = int(input("Enter Marks for Hindi: "))

total = english + maths + science + social + hindi

print("Total Marks:", total)
print("Percentage:", (total / 500) * 100)

#8) To Convert Temp from celsius to fahrenheit
celsius = float(input("Enter Temperature in celsius : "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#9) To Convert Temp from fahrenheit to celsius
fahrenheit = float(input("Enter Temperature in fahrenheit : "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Fahrenheit:", celsius)


#10) Swapping of 2 numbers using 3rd variable
a = 20
b = 30

temp = a
a = b 
b = temp 
print("value of a : ", a,"value of b : ", b)

#11) Swapping of 2 numbers without using 3rd variable
a = 20
b = 30

a = a + b
b = a - b
a = a - b

print("value of a : ", a,"value of b : ", b)

#12) Swapping of 2 numbers without using 3rd variable with divide and multiply
a = 20
b = 30

a = a * b
b = a / b
a = a / b
print("value of a : ", a,"value of b : ", b)