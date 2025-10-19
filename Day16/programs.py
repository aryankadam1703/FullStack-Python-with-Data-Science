# #create a tuple
# t = (10, 20, 30, 40, 50)
# print(t)  

# #create a tuple with single value
# t_single = (10,)
# print(t_single)
# print(type(t_single))  # <class 'tuple'>

# #create tuple without round brackets
# t_no_brackets = 10, 20, 30, 40, 50
# print(t_no_brackets)  
# print(type(t_no_brackets))  # <class 'tuple'>

# #Size of tuple, list and set
# from sys import getsizeof
# t = (10, 20, 30, 40, 50)
# l = [10, 20, 30, 40, 50]
# s = {10, 20, 30, 40, 50}
# print(getsizeof(t))
# print(getsizeof(l))
# print(getsizeof(s))

# #1.add and delete elements in a tuple

word = "India"

for i in range(1, len(word) + 1):
    for j in range(i):
        print(word[j], end=" ")
    print()