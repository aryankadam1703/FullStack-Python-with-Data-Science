#1. create a list containing the names of five different fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

#2. add a new fruit to the list at end
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("watermelon")
print(fruits)

#3. remove one fruit from the index 2
fruits = ["apple", "banana", "cherry", "date", "watermelon"]
fruits.pop(2)
print(fruits)

#4. Access and print the third fruit in the list
fruits = ("apple", "banana", "cherry", "date")
print(fruits[2])

#5. create a tuple containing three different colors
colors = ("red", "green", "blue")
print(colors)

#6. convert the tuple into list
fruits = ("apple", "banana", "cherry", "date", "watermelon")
l = list(fruits)
print(l)

#7. add all elements from tuple to list
l = ["apple", "banana", "cherry"]
fruits = ("date", "elderberry", "fig")
l.extend(fruits)
print(l)

#8. check length of the list and tuple
fruits = ("apple", "banana", "cherry", "date", "watermelon")
l = ["apple", "banana", "cherry"]
print(len(fruits))  
print(len(l))      

#9. check size of list and tuple 
from sys import getsizeof
fruits = ("apple", "banana", "cherry", "date", "watermelon")
l = ["apple", "banana", "cherry"]
print(getsizeof(fruits))
print(getsizeof(l))

#10. check memory address of list and tuple
fruits = ("apple", "banana", "cherry", "date", "watermelon")
l = ["apple", "banana", "cherry"]
print(id(fruits))
print(id(l))    

#11. write a program to find the maximum and minimum in tuple
t = (10, 20, 30, 40, 50)
print(max(t))  
print(min(t))

#12. write a program to flatten a nested tuple
nt = ((1, 2), (3, 4), (5, 6))
flat_tuple = tuple(item for sublist in nt for item in sublist)
print(flat_tuple)

#13. write a program to reomve duplicates from a tuple
t = (1, 2, 2, 3, 4, 4, 5)
t_no_duplicates = tuple(set(t))
print(t_no_duplicates)

#14. write a program to merge two tuples and sort the merged tuple
t1 = (3, 1, 4)
t2 = (2, 5, 6)
mt = t1 + t2
print(mt)
mt_sorted = tuple(sorted(mt))
print(mt_sorted)

#15. find second largest number in a tuple
t = (10, 20, 30, 40, 50)
st = sorted(t)
sl = st[-2]
print(sl)

#16. check two tuples are equal
t1 = (1, 2, 3, 4, 5)
t2 = (2, 3, 4, 1, 5)
print(t1 == t2)

#17. find common elements in two tuples
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
common = tuple(set(t1).intersection(set(t2)))
print(common)

#18. 