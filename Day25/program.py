# #1. square of 1 -5 numbers 
# l = [1, 2, 3, 4, 5]

# sq = list(map(lambda s : s**2,l))
# print(sq)

# #2. To display cube of 1 - 5 number using map functions
# no = [1, 2, 3, 4, 5]

# cb = list(map(lambda s : s**3,no))
# print(cb)

# #3. to convert name to uppercase
# name = ['john','blake','martin','tiger']

# up = list(map(lambda s : s.upper(), name))
# print(up)

# #4. to calculate length of string
# name = ['john','blake','martin','tiger']

# legnth = list(map(lambda s : len(s), name))
# print(legnth)

# #5. to increase marks by five
# marks = [35,67,80,56,65]

# a = list(map(lambda s : s+5, marks))
# print(a)

# #6. To increase salary by 10000 sing map function
# emp = {'john':34000,'blake':50000,'martin':67000,'tiger':23000}

# b = dict(map(lambda s : (s[0], s[1]+10000), emp.items()))
# print(b)

# #7. to decrease marks by 5 
# emp = {'john':45,'blake':50,'martin':67,'tiger':88}

# s = dict(map(lambda s : (s[0], s[1]-5), emp.items()))
# print(s)

# #8. to discount product price by 25%
# product = {"mobile":25000, "Laptop":56000, "TV":45000, "AC":23000}

# d = dict(map(lambda s : (s[0],(s[1]-s[1]*25/100)), product.items()))
# print(d)

#9. Add two Lists element-wise using lambda function
a = [1, 2, 3]
b = [4, 5, 6]

add = list(map(lambda x,y : x+y, a,b))
print(add)

#10. Combine the names from two list to form full name
f_n = ['John', 'Jane','Alice']
l_n = ['Doe','Smith','Wonderland']

full = list(map(lambda a,b : a+' '+b, f_n,l_n))
print(full)

#11. Check palindrome in a list
words = ['madam','racecar','level','python']

palindrome = list(map(lambda w : w==w[::-1], words))
print(palindrome)

#task
#1.