#Agenda - Dictionary Logical Questions

#methods of dictionary
#keys(), values(), items()
# student = {'name': "Aryan", 'rollno': 101, 'age': 20, 'city': "Delhi"}
# print(student.keys())

# for i in student.keys():
#     print(i)             #keys

# for i in student.values():
#     print(i)             #values

# for i in student.items():
#     print(i)             #tuple of key:value pairs

# #1. Write a program to summ all the items in a dictionary
# marks = {'sub1': 90, 'sub2': 80, 'sub3': 85, 'sub4': 95}

# sum = 0
# for i in marks.values():
#     sum += i

# print("Total Marks:", sum)

# #or 
# s = sum(marks.values())
# print("Total Marks:", s)

# #2. Write a program to multiply all the items in a dictionary
# marks = {'sub1': 90, 'sub2': 80, 'sub3': 85, 'sub4': 95}

# m = 1
# for i in marks.values():
#     m *= i

# print("Total Marks:", m)

# #3. Write a program to convert two lists into a dictionary
# keys = ["one", "two", "three", "four", "five"]
# values = [1, 2, 3, 4, 5]
# d = dict(zip(keys, values))
# print("Dictionary:", d)

# #4. Write a program to print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of the keys
# d = {}

# for i in range(1, 6):
#     d[i]=i**2

# print("Dictionary with squares:",d)

# #5. write a program to merge two dictionaries
# emp1 = {'name': 'Alice', 'age': 30}
# emp2 = {'department': 'HR', 'salary': 50000}

# m = emp1.update(emp2)
# print(emp1)

# #6. Display Max and minimum value in a dictionary
# marks = {'sub1': 90, 'sub2': 80, 'sub3': 85, 'sub4': 95}
# max_v = max(marks.values())
# min_v = min(marks.values())
# print("Maximum Marks:", max_v)
# print("Minimum Marks:", min_v)

# #7. Write a program to display subjects whose marks are greater than 60
# marks = {'sub1': 67, 'sub2': 56, 'sub3': 44, 'sub4': 77}
# d = {}

# for sub,marks in marks.items():
#     if marks > 60:
#         print(sub, ":", marks)
#         l = {sub:marks}
#         d.update(l)

#8. to display students who lives in pune
students = {'john': 'pune', 'black': 'mumbai', 'tiger': 'pune', 'joe': 'delhi'}
d = {}

for stud,city in students.items():
    if city == 'pune':
        l = {stud:city}
        d.update(l)

print("Students from Pune:", d)

#9. Write a program to filter the height and weight of students,
# Height > 6ft and Weight > 70kg
dict2 = {'Cierra Vega': (6.2, 71), 'Alden Cantrell': (5.9, 65),
          'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66), 'John Doe': (6.1, 72)}
d = {}

for i, j in dict2.items():
    h,w = j
    if h > 6 and w > 70:
        l = {i:j}
        d.update(l)
print(d)

#10. Write a program to sort (ascending and descending) a dictionary by its values.
marks = {'sub1': 90, 'sub2': 80, 'sub3': 85, 'sub4': 95}

asc = sorted(marks.values())
print(asc)

dsc = sorted(marks.values(), reverse=True)
print(dsc)

#11. Counting the word frequency in a string
text = "hello world hello everyone welcome to the world of programming"
word_count = {}

word = text.split()

for i in word:
    if i not in word_count.keys():
        word_count[i] = 1
    else:
        word_count[i]=word_count[i]+1
print(word_count)