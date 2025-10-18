#Agenda

1. Sets - comma seperated values inside curly brackets
syntax
set_name = {"value1", "Value2",..........}

eg:-
    s1 = {10,20,30,40}

# Properties
    1. Unordered - indexing / slicing not applicable
    2. mutable - not changeable ------insert and delete possible only
                                  updation is not possible
    3. heterogenous collection of immutable elements where insertion order of immutable elements is allowed
        eg:- s1 = {10, 10.56, 3+4j, [10,20,30]}  # not allowed because of mutable list
             s1 = {10, 10.56, 3+4j, (10,20,30)}  # allowed 
    4. duplicate elements not allowed

# Set Methods
# How to insert elements in set
    1. add() - insert elements in set
        syntax - varname.add()

    2. update() - to add multiple elements in set / join two sets (Concatenation)
        syntax - varname1.update(varname2)

# Updation not allowed in sets

# Delete elements methods
    1.remove() - if element is not present in set then remove throws error
        syntax = varname.remove("value")
    2.discard() - if element is not present in set then discard will not throws error
        syntax = varname.discard("value")
    3. pop() - randomly deletes a element 
        syntax = varname.pop()
    4. clear() - empty set
        syntax = varname.clear()

# create empty set
    1. set() - empty set

# Set merge methods
    1. union() - merge all elements, duplicate will be printed only once
        syntax - var1.union(var2)
    2. intersection() - merge only common elements from sets 
        syntax - var1.intersection(var2)
    3. difference() - returns elements that are in var1 but not in var2
        syntax - var1.difference(var2)
    4. difference_update() -
    5. symmetri_difference() - it will return a new set of elements that are in either of the sets but not in both.
    6. symmetri_difference_update() -
    