# 1. Convert a list of integers to their squares using map().
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)  


# 2. Convert a list of string numbers to actual integers using map().
str_nums = ["1", "2", "3", "4"]
ints = list(map(int, str_nums))
print(ints)  


# 3. Capitalize all the words in a list using map().
words = ["apple", "banana", "cherry"]
cap_words = list(map(str.capitalize, words))
print(cap_words) 


# 4. Convert a list of temperatures in Celsius to Fahrenheit using map().
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit) 


# 5. Find the length of each word in a list using map().
words = ["python", "map", "function"]
lengths = list(map(len, words))
print(lengths)


# 6. Add corresponding elements of two lists using map().
a = [1, 2, 3]
b = [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, a, b))
print(sum_list)


# 7. Convert a list of full names to uppercase using map().
names = ["john doe", "jane smith"]
upper_names = list(map(str.upper, names))
print(upper_names)  


# 8. Reverse each string in a list using map().
words = ["python", "map", "reverse"]
reversed_words = list(map(lambda x: x[::-1], words))
print(reversed_words) 


# 9. Multiply all numbers in a list by 10 using map().
nums = [1, 2, 3, 4, 5]
mul_by_10 = list(map(lambda x: x * 10, nums))
print(mul_by_10) 

# 10. Replace all spaces with dashes in a list of strings using map().
sentences = ["hello world", "python map function"]
replaced = list(map(lambda x: x.replace(" ", "-"), sentences))
print(replaced)  # ['hello-world', 'python-map-function']


# 11. Convert a list of float numbers to integers using map().
floats = [1.2, 3.4, 5.6]
ints = list(map(int, floats))
print(ints)  # [1, 3, 5]


# 12. Append the string "!" to each word in a list using map().
words = ["hi", "hello", "python"]
exclaimed = list(map(lambda x: x + "!", words))
print(exclaimed)  # ['hi!', 'hello!', 'python!']


# 13. Convert a list of date strings to datetime.date objects using map().
from datetime import datetime
dates = ["2025-07-23", "2025-08-29"]
date_objs = list(map(lambda d: datetime.strptime(d, "%Y-%m-%d").date(), dates))
print(date_objs)  # [datetime.date(2025, 7, 23), datetime.date(2025, 8, 29)]


# 14. Count the number of vowels in each word in a list using map().
words = ["cherry", "banana", "apple", "berries"]
vowel_counts = list(map(lambda w: sum(1 for ch in w if ch in 'aeiou'), words))
print(vowel_counts)  # [1, 3, 2, 3]


# 15. Apply a list of functions to a single number using map().
def square(x): return x**2
def cube(x): return x**3
def double(x): return x*2

funcs = [square, cube, double]
num = 3
results = list(map(lambda f: f(num), funcs))
print(results)  # [9, 27, 6]
