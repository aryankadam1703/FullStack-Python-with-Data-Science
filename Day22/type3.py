# Remaining types of functions
    #3. With return type without parameters
    # need to store the return answer in a variable to print

def add():
    a = 20
    b = 30
    c = a + b
    return c

a = add()
print(a)

#or 
print(add())

#1. area of rectangle
def rectangle():
    l = int(input("Length: "))
    b = int(input("Breadth: "))

    area = l * b
    return area

rect = rectangle()
print(rect)

#2. factorial
def fact():
    n = int(input("Enter Number for factorial : "))
    f = 1

    for i in range(1, n+1):
        f = f * i
    return f

f = fact()
print(f)

#3 3 no greater
def greater():
    a = 10
    b = 20
    c = 30

    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greater())

