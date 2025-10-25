#task 
#1. palindrom

def palindrom():
    n = input("Enter to check plaindrom or not: ")

    if n == n[::-1]:
        print(n, "is palindrom")
    else:
        print("Not a palindrom")

palindrom()

#2. armstrong no

def armstrong():
    n = int(input("Enter number to check armstrong number: "))
    temp = n
    sum = 0
    power = len(str(n))

    for i in range(n):
        r = n % 10
        sum += (r**power)
        n = n // 10
    print(sum)

    if temp == sum:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong()

#3. prime no()
def prime():
    n = int(input("Enter number to check prime: "))
    if n < 2:
        print(n, "is not a prime number")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
    print(n, "is a prime number")

prime()

#4. fibonacci series
def fibonacci():
    n = int(input("Enter Number to get fibonacci series: "))

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci()