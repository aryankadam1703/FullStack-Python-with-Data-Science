# #1. Write a Python program to count the number of strings from a given list of strings. 
# # The string length is 2 or more and the first and last characters are the same.

# sample_list = ['level', 'xyz', 'aba', '1221', 'nitin']

# count = 0
# matching_str = []

# for i in sample_list:
#     if len(i) > 2 and i[0] == i[-1]:
#         count+=1
#         matching_str.append(i)

# print("Matching Count", count)
# print("Matching Strings:", matching_str)

# #2 Write a Python program to clone or copy a list.
# a = [10, 20, 30, 40]
# b = []

# for i in a:
#     b.append(i)

# print(b)

# #3 Write a Python function that takes two lists and returns True I
# # if they have at least one common member.

# list1 = [10, 20, 30, 40, 50]
# list2 = [10, 40, 50, 60, 70]
# value = False
# for i in list1:
#     if i in list2:
#         value = True
#         break
# print(value)

# #4 Write a Python program to print a specified list after removing the # 0th, 4th and 5th elements.
# # Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # Expected Output: ['Green', 'White', 'Black']
# # Sample list
# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# color_list.pop(5)
# color_list.pop(4)
# color_list.pop(0)

# print(color_list)

# print()

# # 5)
# # Write a Python program to get unique values from a list.
# # To remove duplicate elements in a list 
# a = [1,2,2,3,4,4,5, "mayur", "mayur"]

# for i in a:
#     if i == i+1:
#         a.remove(a[i+1])
# print(a)

# #6 Join two list
# #method 1
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = [*list1, *list2]
# print(result)

# #method 2 concatenation
# add = list1 + list2
# print(add)


#Interview Questions
# 1) What is a list in Python?
# 2) How do you create a list in Python?
# 3) Can a Python list contain elements of different data types? Give an example.
# 4) How can you access elements in a list? Explain with examples using indexing and slicing.

a= 'The Kiran Academy'
print(a[-6:])    