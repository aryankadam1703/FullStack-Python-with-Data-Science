#1. add a list of elements to a set
fruits = set()
fruits.update({"mango", "apple", "banana", "cherry"})
print(fruits)    

#2. Return a new set of identical items from two sets
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}
f3 = f1.intersection(f2)
print(f3)         #{'banana'}

#3. Get only unique from two sets
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}

print(f1.symmetric_difference(f2))

#4. Update the first set with items that does not exist in the second set
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}

print(f1.difference_update(f2))
print(f1)         #{'cherry', 'apple', 'mango'}

#5. Remove items from the set at once
f1 = {"mango", "apple", "banana", "cherry"}
f1.clear()
print(f1)

#6. Return a set of elements present in Set A or B, but not both
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}

symmetri_diff = f1.symmetric_difference(f2)
print(symmetri_diff)

#7. Check if two sets have any elements in common
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}
print(f1.isdisjoint(f2)) 
print(f1.intersection(f2))

#8. Update set1 by adding items from set2, except common items
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melo"}

symmetric_diff = f1.symmetric_difference_update(f2)
print(f1)

#9. Remove items from set1 that are not common to both set1 and set2
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}
f1.intersection_update(f2)
print(f1)         #{'banana'}
f1.symmetric_difference(f2)

#10. find the size of a set
f1 = {"mango", "apple", "banana", "cherry"}
print(len(f1))

#11. Iterate over a set in python
fruits = {"mango", "apple", "banana", "cherry"}
for i in fruits:
    print(i)

#12. Max and Min in a set
fruits = {10, 20, 30, 40, 50}
print(max(fruits))
print(min(fruits))

#13. Removce items from set
fruits = {"mango", "apple", "banana", "cherry"}
fruits.remove("mango")
fruits.discard("apple")
fruits.pop()  # Randomly removes an item
print(fruits) 

#14. check if two lists have atleast one common element
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
set1 = set(list1)
set2 = set(list2)
common= set1.intersection(set2)
print(common)

#15. to find common elements in three lists using sets
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
common = set1.intersection(set2).intersection(set3)
print(common) 

#16. find missing and additional elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
missing = set1.difference(set2)
additional = set2.difference(set1)
print("Missing elements:", missing)
print("Additional elements:", additional)

#17. difference between two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
d = set1.difference(set2)
print("Difference:", d)

#18. set difference to find element from a duplicated array
array = [1, 2, 2, 3, 4, 5, 5]
sett = set(array)
print("Unique elements:", sett)