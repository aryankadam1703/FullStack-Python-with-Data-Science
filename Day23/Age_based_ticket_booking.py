age = int(input("Enter your age"))

if age < 5:
    price = 0
elif age < 18:
    price = 100
elif age < 60:
    price = 200
else:
    price = 150

print(f'Your ticket price is : {price}')