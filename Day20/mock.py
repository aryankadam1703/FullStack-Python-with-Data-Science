# balance = float(input("Enter your bank balance:"))

# while True:
#     print("""
#         1. Check Balance
#         2. Deposite
#         3. Withdraw
#         4. Exit""")
    
#     ch = int(input("Enter your choice: "))

#     if ch==1:
#         print("Your balance is :",balance)
#     if ch==2:
#         d = float(input("Enter the amount you want to deposite: "))
#         balance += d
#         print("Your deposite is successful", balance)
#     if ch==3:
#         w = float(input("Enter the amount you want to Withdraw: "))
#         if w < balance:
#             balance = balance - w
#         print("Your deposite is successful", balance)
#     if ch==4:
#         print("Thank You!!! Visit Again")
#         break

#2.
import random

# n = random.randint(1, 10)
n = 7

chances = 0

while True:
    i = int(input("Enter your number: "))

    if n < i:
        print("Greater")
    elif n > i:
        print("Smaller")
    else:
        print("Correct!!!")