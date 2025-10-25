#Without return type with parameters

#1. area of rectangle
def area_rectangel(l, b):
    area = l * b
    print(area)

area_rectangel(20, 30)

#2. Area of circle
def area_circle(r):

    area = 3.14 * (r**2)
    print(area)

area_circle(4)

#3. Factorial
def fact(n):
    f = 1

    for i in range(1, n+1):
        f *= i
    print('factorial : ', f)

fact(4)

#4. Greater Number
def greater(a, b, c):
    if a>b and a>c:
        print("a is greater")
    elif b>a and b>c:
        print("b is greater")
    else:
        print('c is greater')

greater(10, 20, 30)