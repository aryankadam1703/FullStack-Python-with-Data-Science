#Hospital Management System

hospital_db = {}

while True:
    print("""
          1. Add Patient Record
          2. Display All Patients
          3. Update Patient Record
          4. Delete Patient Record
          5. Search by Disease
          6. Search by Name
          7. Exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        city = input("Enter City: ")
        hospital_db[patient_id] = {
            'name': name,
            'age': age,
            'disease': disease,
            'city': city
        }
        print("Patient record added successfully.")
    elif choice == 2:
        print('-'*90)
        print('{:^15}|{:^20}|{:^10}|{:^20}|{:^20}|'.format("Patient ID", "Name", "Age", "Disease", "City"))
        print('-'*90)
        for pid, details in hospital_db.items():
            print('{:^15}|{:^20}|{:^10}|{:^20}|{:^20}|'.format(pid, details['name'], details['age'], details['disease'], details['city']))
    elif choice == 3:
        pid = int(input("Enter Patient ID to update: "))
        if pid in hospital_db:
            print("""
                1. Update Name
                2. Update Age
                3. Update Disease
                4. Update City
            """)
            upd_choice = int(input("Enter your choice: "))
            if upd_choice == 1:
                hospital_db[pid]['name'] = input("Enter new name: ")
                print("Name updated successfully.")
            elif upd_choice == 2:
                hospital_db[pid]['age'] = int(input("Enter new age: "))
                print("Age updated successfully.")
            elif upd_choice == 3:
                hospital_db[pid]['disease'] = input("Enter new disease: ")
                print("Disease updated successfully.")
            elif upd_choice == 4:
                hospital_db[pid]['city'] = input("Enter new city: ")
                print("City updated successfully.")
            else:
                print("Invalid update choice.")
        else:
            print("Patient ID not found.")
    elif choice == 4:
        pid = int(input("Enter Patient ID to delete: "))
        if pid in hospital_db:
            del hospital_db[pid]
            print("Patient record deleted successfully.")
        else:
            print("Patient ID not found.")
    elif choice == 5:
        search_disease = input("Enter disease to search: ")
        found = False
        for pid, details in hospital_db.items():
            if details['disease'].lower() == search_disease.lower():
                print(f"Patient ID: {pid}, Name: {details['name']}, Age: {details['age']}, City: {details['city']}")
                found = True
        if not found:
            print("No records found for this disease.")
    elif choice == 6:
        search_name = input("Enter name to search: ")
        found = False
        for pid, details in hospital_db.items():
            if details['name'].lower() == search_name.lower():
                print(f"Patient ID: {pid}, Disease: {details['disease']}, Age: {details['age']}, City: {details['city']}")
                found = True
        if not found:
            print("No records found for this name.")
    elif choice == 7:
        print("Exiting Hospital Management System.")
        break
    else:
        print("Please enter a valid choice.")

