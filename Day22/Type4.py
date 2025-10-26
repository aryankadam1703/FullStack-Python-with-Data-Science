# With Return ty with parameters 

#1. area of rectangle
def area_rectangle(l, b):
    area = l * b
    return area

rect = area_rectangle(50, 60)
print(rect)

#2. factorial
def fact(n):
    f = 1

    for i in range(1, n+1):
        f *= i
    return f

print(fact(4))

#3 3 no greater
def greater(a, b, c):

    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greater(80,50,60))

#4. armstrong number
def armstrong(n):
    temp = n
    power = len(str(n))
    sum = 0

    for i in range(n):
        r = n % 10
        sum = sum + (r**power)
        n = n // 10
    return sum

n = 153
if armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")

#5. palindrome no
def palindrome_no(n):
    temp = n
    reverse = 0

    while n > 0:
        r = n % 10
        reverse = reverse * 10 + r
        n = n // 10
    return reverse == temp

n = 12345

if palindrome_no(n):
    print("Palindrome")
else:
    print("Not palidrome")

#6. To print armtrong from given list 
l = [407, 459, 234, 1005, 153, 370, 371]
for num in l:
    num1 = str(num)
    l = len(num1)
    sum = 0
    for i in num1:
        sum = sum + int(i)**l
    if num == sum:
        print(num)

#7. To find perfect number from given list
l = [6, 12, 34, 56, 28, 103]

for num in l:
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum+= i
    
    if sum == num:
        print(num, "is a Prefect Number")
    else:
        print(num, "is not perfect number")  

  
