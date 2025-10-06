a = int(input("Enter first number: "))
print(type(a))
b = int(input("Enter second number: "))
print(type(b))

c = a + b
print("Sum of numbers :", c)
print(type(c))


#2) calculate area of rectangle, area of cirle
a = int(input("Enter length of rectangle: "))
b = int(input("Enter width of rectangle: "))

area_of_rectangle = a * b
print("Area of rectangle:", area_of_rectangle)

#area of circle
r = int(input("Enter radius of circle: "))

area_of_circle = 3.14 * r * r
print("Area of circle:", area_of_circle)

#3) To accept 5 subject marks and calculate Sum and percentage
S1 = eval(input("Enter marks for English: "))
S2 = eval(input("Enter Marks for Maths: "))
S3 = eval(input("Enter Marks for Science: "))

Sum = S1 + S2 + S3
print("Sum of marks:", Sum)

percentage = (Sum / 300) * 100
print("Percentage of marks:", percentage)


#4) To calculate Simple Interest and compound Interest
P = eval(input("Enter Principal amount: "))
N = eval(input("Enter Number of years: "))
R = eval(input("Enter Rate of interest: "))


simple_interest = (P * N * R) / 100
print("Simple Interest:", simple_interest)

compund_interest = P * ((1 + (R / 100)) ** N) - P
print("Compound Interest:", compund_interest)

#5) To calculate volumn of cone
r = eval(input("Enter radius of cone: "))
h = eval(input("Enter height of cone: "))

volume_of_cone = (1/3) * 3.14 * r * r * h
print("Volume of Cone:", volume_of_cone)

#6) swapping of 2 numbers
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))

temp = a
a = b
b = temp
print("After swapping, first number:", a , "second number:", b)


