#Task 1:

students = {
    101 : {'name': 'Aryan', 'age': 20, 'marks': 85},
    102 : {'name': 'Harsh', 'age': 22, 'marks': 90},
    103 : {'name': 'Kaustubha', 'age': 21, 'marks': 88},
    104 : {'name': 'Rohan', 'age': 23, 'marks': 92}
}

print(students)

#1. add new record to students
x = students[105] = {'name': 'Vedant', 'age':22, 'marks':92}
print(students)

#2. update record of student with rollno 102
students[102]['age'] = 23
students[103]['marks'] = 95
print(students)

#3. remove a record by roll no
del students[104]
print(students)

#4. Find details of student by roll no from students dictionary
x = students[101]
print(x)

#5. display all students details neatly
for i in students:
    print(f"Roll No: {i}, Name: {students[i]['name']}, Age: {students[i]['age']}, Marks: {students[i]['marks']}")


#Task 2: