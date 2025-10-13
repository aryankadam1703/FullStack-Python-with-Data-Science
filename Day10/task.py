# #1) fibonacci series

# fs = 7
# a=0
# b=1

# for i in range(fs):
#     print(a, end=" ")
#     a, b= b, a+b

# #2) Reverse Number

# n = 12345
# reverse = 0

# length = len(str(n))

# for i in range(length):
#     length = n % 10
#     reverse = reverse * 10 + length
#     n = n // 10

# print(reverse)

# #3)Sum of digits
# n = int(input("Enter Number : "))
# sum = 0

# for i in range(n):
#     r = n % 10
#     sum += r
#     n = n // 10
# print(sum)

# #4) Armstrong Number
# n = int(input("Enter Number : "))
# temp = n
# sum = 0
# power = len(str(n))

# for i in range(n):
#     r = n % 10
#     sum = sum + (r**power)
#     n = n // 10

# if(sum == temp):
#     print("Number is armstrong")
# else:
#     print("Not Armstrong")

# print(sum)


#5) Palindrome Number
n = int(input("Enter Number: "))
temp = n
reverse = 0

while n > 0:
    a = n % 10
    reverse = reverse * 10 + a
    n = n // 10

if(temp == reverse):
    print("palindrome")
else:
    print("Not palindrome")

#6 Prime Number
import math

n = int(input("Enter numbers: "))

if n<=1:
    print("Not a Prime number")
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n % 2 == 0:
            print("Not a prime number")
        else:
            print("Prime Number")

#7 Perfect number
n = int(input("Enter numbers: "))

sum = 0

for i in range(1,n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print(n, " is a Perfect Number.")
else:
    print(n, " is Not a Perfect Number.")