# Without return type without parameters

def Hello():
    print("Hello")

def good():
    print("Good Morning")

def Bye():
    Hello()
    print("Bye.......")


Hello()
good()
Bye()

#1. Addition of two numbers using function

def add():
    a = 10
    b = 20
    c = a + b
    print(c)

def sub():
    a = 10
    b = 20
    c = b - a
    print(c)

def mul():
    a = 10
    b = 20
    c = a * b
    print(c)

add()
sub()
mul()

#2. area of rectangle
def area_rectangel():
    l = int(input("Enter length: "))
    b = int(input("Enter Breadth: "))

    area = l * b
    print(area)

area_rectangel()

#3. Area of circle
def area_circle():
    r = int(input("Enter radius: "))

    area = 3.14 * (r**2)
    print(area)

area_circle()

#4. Factorial
def fact():
    n = int(input("Enter Number : "))
    f = 1

    for i in range(1, n+1):
        f *= i
    print('factorial : ', f)

#5. greate number amount 3

def greater():
    a = 10
    b = 20
    c = 30

    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print('c is greater')

greater()

#6. Calculations program with Menu

def add():
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    c = a + b
    print(c)

def sub():
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    c = b - a
    print(c)

def mul():
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    c = a * b
    print(c)

def div():
    a = int(input("Enter 1st Number"))
    b = int(input("Enter 2nd Number"))
    c = a / b
    print(c)

while True:
    print("""
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division""")
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    else:
        print("Enter valid choice")