# #1. Strip()
# str = "   Hello   "
# print(str.strip())

# #2. replace()
# str = "hello world"
# print(str.replace('hello', 'good'))

# #3. join(iterable)
# # Join elements of an iterable(like a list) into a string with a sequence
# words = ["Python", "is", "a", "fun"]
# print(" ".join(words))

# #4. Write a program to chech enter passsword and confirmed password is equal or not
# password = input("Enter Password: ")
# con_password =input("Enter you password again: ")

# if password == con_password:
#     print("Same")
# else:
#     print("Not Same")

#5 To count no of uppercase and lowercase character
a = "Kiran Academy"
upper = 0
lower = 0
for i in a:
    if(i.isupper()):
        upper += 1
    elif(i.islower()):
        lower += 1

print("Upper Count",upper)
print("Lower Count", lower)