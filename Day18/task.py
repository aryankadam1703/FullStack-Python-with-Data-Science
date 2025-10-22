#1. Create a Dictionary named student with the following information: name, age and grade.

student = {'name': 'John', 'age':29, 'grade': 'A'}
print(student)

#2. Access a value - from student dictionary, access the value of the key 'grade'.
grade = student['grade']
print(grade)

#3. Add a new key-value pair to the student dictionary: 'school' with the value of your choice.
student = {'name': 'John', 'age':29, 'grade': 'A'}

student['school'] = "city international school"
print(student)

#4.. Update a value - change the value of the key 'age' key in the student dictionary to a new value.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

student['age'] = 23 
print(student)

#5. Delete a key - remove the key 'grade' from the student dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

del student['grade']
print(student)

#6. loop through the dictionary and print each key-value pair.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

for key,value in student.items():
    print(key, ":", value)

#7. check for a key - check if the key 'name' exists in the student dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

if 'name' in student:
    print("name key exists in student dictionary")
else:
    print("Not present")

#8. Dictonary Length - Print the number of key-value paris in the dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

print(len(student))

#9. Copy a Dictionary - create a copy of the student dictionary and name it student_copy.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

stucdent_copy = student.copy()
print(stucdent_copy)

#10. Nested Dictionary - Create a dictionary named classroom that contains two students, each student is a dictionary with keys: 'name' and age.
classroom = {
    'student 1' : {'name':'Subodh', 'age':23},
    'student 2' : {'name':'Aryan', 'age':22}
}

print(classroom)

#11. Convert two list into dictionary.
keys = ["name", "rollno", "age", "grade"]
values = ["john", 1, 29, 'A']

j = dict(zip(keys, values))
print(j)

#12. Merge two dictionaries into one dictionary.
dict1 = {'name': 'Alice', 'age': 30}
dict2 = {'department': 'HR', 'salary': 50000}

m = dict1.update(dict2)
print(dict1)

#13. Print value of key 'history' from the below dictionary.
marks = {'math': 90, 'science': 85, 'history': 88, 'english': 92}

print(marks['history'])

#14. Initialize a dictionary with default values.
default = dict.fromkeys(['name', 'age', 'grade'], 'N/A')
print(default)

#15. Create a dictionary by extracting the keys from a given dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

keys = student.keys()
print(keys)

#16. Delete a list of keys from a dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}
del student['grade']
del student['school']
print(student)

#or

keys = ['grade', 'school']
for k in keys:
    if k in student:
        del student[k]

#17. Check if a value exists in a dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

if 'John' in student.values():
    print("John present in dictionary")
else:
    print("Not present")

#18. Rename a key of a dictionary.
student = {'name': 'John', 'age':29, 'grade': 'A', 'school':"city international school"}

student['My_name'] = student.pop('name')
print(student)

#19. Get the key of a minimum value in a dictionary.
marks = {'sub1': 90, 'sub2': 80, 'sub3': 85, 'sub4': 95}
min_key = min(marks, key=marks.get)
print(min_key)

#20. Change the value of a key in a nested dictionary.
classroom = {
    'student 1': {'name': 'Subodh', 'age': 23},
    'student 2': {'name': 'Aryan', 'age': 22}
}

classroom = {
    'student 1': {'name': 'Subodh', 'age': 23},
    'student 2': {'name': 'Aryan', 'age': 22}
}

classroom['student 1']['age'] = 29
classroom['student 2']['age'] = 30
print(classroom)