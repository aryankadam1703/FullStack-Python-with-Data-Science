student = {'name': "Aryan", 'rollno': 101, 'age': 20, 'city': "Delhi"}
print(student)
print(type(student))

s = {10,20.45,True,"Aryan"} #set

#Access the elements of dictionary
print(student['name'])
print(student['rollno'])

#create a dicionary of employee
employee = {'name': "Aryan", 'age':20, 'department': "IT", 'salary': 50000}
print(employee)

#creaete empty dictionary and add elements
emp = {}

#add elements to emp dictionary
emp['id'] = 101
emp['name'] = "John"
emp['department'] = "HR"
emp['salary'] = 60000
print(emp)

#add new key-value pair to emp
student = {'name': "Aryan", 'rollno': 101, 'age': 20, 'city': "Delhi"}
student['marks'] = 85
print(student)

#change / update values in dictionary
student['age'] = 21
print(student)

#create a dicitonary with state and cities
states = {'Maharashtra': ['Mumbai', 'Pune', 'Nagpur'], 
        'karnataka': ["Banglore", "Mysore", "Mangalore"], 
        'Tamil Nadu': ["Chennai", "Coimbatore", "Madurai"],
        'Rajasthan': ["Jaipur", "Udaipur", "Jodhpur"]}
print(states)

ky = states.keys()
vl = states.values()
print(ky)
print(vl)

#create a nested dictionary of car
car = {
    'ford': {'mustang': {'year': 2020, 'airbags': 2, 'color': 'red'},
             'endavour' : {'year': 2021, 'airbags': 2, 'color': 'blue'}},
    'toyota': {'fortuner': {'year': 2022, 'airbags': 2, 'color': 'black'},
               'innova': {'year': 2023, 'airbags': 2, 'color': 'white'}},
    'honda': {'city': {'year': 2021, 'airbags': 2, 'color': 'silver'},
                'jazz': {'year': 2020, 'airbags': 2, 'color': 'grey'}}
}
print(car)

#accessing nested dictionary
print(car['ford']['mustang']['year'])
print(car['honda']['jazz']['color'])

#change value in nested dictionary
car['ford']['mustang']['year'] = 2021
car['toyota']['fortuner']['color'] = 'white'
print(car)
