# add two numbers using normal function
def add():
    a= 10
    b= 20
    c = a + b
    print(c)

add()

#using lambda function
a = lambda a=10,b=20 : a+b
print(a())

#square of numbers using lambda function
n = int(input("Enter number : "))
sq = lambda n : n**2
print(sq(n))

#1. Cube of given number using normal and lambda function
def cube():
    i = int(input("Enter Number to get cube: "))
    cb = i ** 3
    print("cube : ", cb)

cube()

#using lambda function
i = int(input("Enter Number to get cube: "))
cb = lambda i : i**3

print(cb(i))

#2.To calculate area of rectangle

area = lambda l=10, b=20 : l*b
print(area())

#3. To calculate area of circle

area_circle = lambda r = int(input("Enter radius: ")) : 3.14*(r**2)
print(area_circle())

#4. To calculate Simple Interest

si = lambda P=40000, R=5, T=2 : (P*R*T)/100
print(si())

#5.To convert string to uppercase
upp = lambda n = input("Enter a string: ") : n.upper()
print(upp())

#6. to calculate length of the string
l = lambda n = input("Enter String: ") : len(n)
print(l())

#7. To extract digits only
ed = lambda str="admin1234" : [i for i in str if i.isdigit()]
print(ed())

#8. To extract alpha only
es =lambda str="admin1234" : [i for i in str if i.isalpha()]
print(es())

#9. Chech if number is even
even = lambda a = 10 : a%2==0
print("Is Even?", even())

#10. Multiply three numbers4
mul = lambda x=10, y=2, z=5 : x*y*z
print(mul())
#11. Reverse a string

reverse = lambda str="Hello" : str[::-1]
print(reverse())

#12. to perform add,sub,mul,div 
add = lambda x= 10, y = 20 : (x+y, x-y, x*y, x/y)

print(add())