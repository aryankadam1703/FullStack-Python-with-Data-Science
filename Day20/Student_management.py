#Student Management System 

db = {
    1 : {'name':'Aryan', 'marks':78, 'course':'Python', 'city':'Pune'},
    2 : {'name':'Subodh', 'marks':90, 'course':'Java', 'city':'Mumbai'},
    3 : {'name':'Vedant', 'marks':80, 'course':'.Net', 'city':'Karad'},
    4 : {'name':'Iliyas', 'marks':95, 'course':'C++', 'city':'Shirwal'} 
}

while True:
    print("""   
          1. Create Records
          2. Display Records
          3. Update Records
          4. Delete Records
          5. Search by Course
          6. Search by Name
          7. Max and Min Marks
          8. Display Marks >= 60
          9. Total Marks
          10. Marks Ascending Order
          11. Marks Descending Order
          12. Exit""")
    
    ch = int(input("Enter Your choice : "))
    if ch == 1:
        details = {}
        rollno = int(input("Enter Roll no : "))
        name =  input("Enter Name : ")
        marks = int(input("Enter marks : "))
        course =  (input("Enter Course : "))
        city =  input("Enter City : ")
        
        details['name'] = name
        details['marks'] = marks
        details['course'] = course
        details['city'] = city

        db[rollno] = details

    elif ch == 2:
        print('-'*110)
        print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format("Roll No", 'Name', 'marks', 'Course', 'City'))
        print('-'*110)

        for rollno in db:
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(rollno, db[rollno]['name'], db[rollno]['marks'], db[rollno]['course'], db[rollno]['city']))
    elif ch == 3:
        rollno = int(input("Enter Roll No: "))
        print("""   
          1. Update Name
          2. Update Makrs
          3. Update Course
          4. Update City
          """)
        c =int(input("Enter your choice: "))
        if c==1:
            un = input("Enter new name : ")
            db[rollno]['name'] = un
            print("Name updated Successfully.............")
        elif c==2:
            um = input("Enter new marks : ")
            db[rollno]['marks'] = um
            print("Marks updated Successfully.............")
        elif c==3:
            uc = input("Enter new Course : ")
            db[rollno]['course'] = uc
            print("Course updated Successfully.............")
        elif c==4:
            ucc = input("Enter new city : ")
            db[rollno]['city'] = ucc
            print("City updated Successfully.............")
        else:
            print("Enter a valid number")
    elif ch==4:
        rollno = int(input("Enter Roll No: "))
        del db[rollno]
        print("record deleted successfully................")
    elif ch==5:
        sc = input("Enter the course name: ")
        for rollno,course in db.items():
            if db[rollno]['course'].lower() == sc.lower():
                print(f'Roll No: {db[rollno]}, Name: {db[rollno]['name']}, Marks: {db[rollno]['marks']}, City: {db[rollno]['city']}')

    elif ch==6:
        sn = input("Enter the course name: ")
        for rollno,name in db.items():
            if db[rollno]['name'].lower() == sn.lower():
                print(f'Roll No: {db[rollno]}, Name: {db[rollno]['name']}, Marks: {db[rollno]['marks']}, City: {db[rollno]['city']}')

    elif ch==7:
        if db:
            marks_list = [details['marks'] for details in db.values()]
            max_marks = max(marks_list)
            min_marks = min(marks_list)
            print(f"Max Marks: {max_marks}")
            print(f"Min Marks: {min_marks}")
        else:
            print("No records available.")

    elif ch==8:
        for rollno, dt in db.items():
            if dt['marks'] > 60:
                print(f"Roll No: {rollno}, Name: {dt['name']}, Marks: {dt['marks']}, Course: {dt['course']}, City: {dt['city']}")
            else:
                print("No students with marks greater than 60")
    elif ch==9:
        total = 0
        for details in db.values():
            total = total + details['marks']
        print(f'Total marks of all studetns: {total}')
    elif ch==10:
        s_db = sorted(db.items())
        for rollno, dt in s_db:
            print(f"Roll No: {rollno}, Name: {dt['name']}, Marks: {dt['marks']}, Course: {dt['course']}, City: {dt['city']}")
    elif ch==11:
        s_db = sorted(db.items(), reverse=True)
        for rollno, dt in s_db:
            print(f"Roll No: {rollno}, Name: {dt['name']}, Marks: {dt['marks']}, Course: {dt['course']}, City: {dt['city']}")
    elif ch==12:
        print("Thank You!!")
        break
    else:
        print("Please enter a valid choice")




