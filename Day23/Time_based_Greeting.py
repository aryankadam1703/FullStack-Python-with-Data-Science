#Time Based Greeting App

hour = int(input("Enter current hour: "))

if 5 <= hour < 12:
    print("Good Morning!!!")
elif 12<= hour < 17:
    print("Good Afternoon!!!")
else:
    print("Good Evening!!!")