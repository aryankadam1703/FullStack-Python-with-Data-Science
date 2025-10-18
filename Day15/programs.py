# #delete methods in set
# fruits = {"mango", "apple", "banana", "cherry"}
# fruits.remove("mango")
# print(fruits)      #{'apple', 'cherry', 'banana'}

# fruits = {"mango", "apple", "banana", "cherry"}
# fruits.discard("mango")
# print(fruits)      #{'apple', 'cherry', 'banana'}

# #create a empty set
# fruits = set()
# print(fruits) 
# fruits.update({"mango", "apple", "banana", "cherry"})
# print(fruits)      #{'apple', 'cherry', 'banana', 'mango'}

# #union
# fruits1 = {"mango", "apple", "banana", "cherry"}
# fruits2 = {"orange", "kiwi", "melon", "banana"}
# fruits3 = fruits1.union(fruits2)
# print(fruits3)     #{'kiwi', 'cherry', 'banana', 'melon', 'apple', 'orange', 'mango'}


# #interection
# f1 = {"mango", "apple", "banana", "cherry"}
# f2 = {"orange", "kiwi", "melon", "banana"}
# f3 = f1.intersection(f2)
# print(f3)         #{'banana'}

#difference 
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}
f3 = f1.difference(f2)
f4 = f1.difference_update(f2)
print(f4)         #{'cherry', 'apple', 'mango'}
print(f3)         #{'cherry', 'apple', 'mango'}

#symmetric_difference
f1 = {"mango", "apple", "banana", "cherry"}
f2 = {"orange", "kiwi", "melon", "banana"}
f3 = f1.symmetric_difference(f2)
f4 = f1.symmetric_difference_update(f2)
print(f4)         #{'kiwi', 'cherry', 'melon', 'apple', 'orange', 'mango'}
print(f3)         #{'kiwi', 'cherry', 'melon', 'apple', 'orange', 'mango'}
