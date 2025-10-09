#1) to check number is positive or negative

n = int(input("Enter a number: "))
if n > 0:
    print("The number is positive")
else:
    print("The number is negative or zero")

#2) to check person is eligible to vote or no
n = int(input("Enter your age: "))

if n >= 18:
    print("yeah! you are eligible to vote")
else:
    print("Sorry! you are not eligible to vote")

#3) to find greater number among two numbers
a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

if a > b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a)

#4) to check if a number is even or odd
a = int(input("Enter number: "))

if a % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#5) to check leap year or not
a = int(input("Enter a year:"))

if (a % 4 ==0 or a % 400 == 0) and (a % 100!=0):
    print("Leap year")
else:
    print("Not a leap year")

#6) to check wether a char is vowel or consonant using if/if else
a = str(input("enter a character: "))

if a in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")

#7) to check number is divisible by 3 or 5
a = int(input("enter a number: "))

if (a % 3 == 0) or (a % 5 == 0):
    print("Divisible")
else:
    print("Not Divisible")

#8) calculate profit or loss
cp = eval(input("Enter cost price: "))
sp = eval(input("Enter selling price: "))

if sp > cp:
    print("Profit:", sp-cp)
else:
    print("Loss:", cp-sp)