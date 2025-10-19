# Agenda
1. Tuples - comma separated values within rounded brackets ()
            round brackets are not compulsry in tuples
    eg:- t = (10,20,30,40,50)

2. Tuple with single values should be mentions using comman after value
    eg :- t = (10,)

3. Properties
    1. Ordered
    2. Immutable - not changeable
    3. Ordered - indexing and slicing is allowed
    4. Duplicate elements is allowed

4. Size of tuple - in bytes
    1. import getsizeof() - returns size of tuples, list, sets etc.
                    based on size we can know the execution speed.
            1. tuples requires less memory and is fast in execution because of immutable
            2. list requires more memory then tuple
            3. dictionary requires more memory than list
            4. set requires more memory then dictionary

5. Supports Packing and Unpacking                          # interview point of view
    1. Packing - Wrapping of multiple values into a single variable
        eg :- x, y, z = 10, 20, 3
              t = x, y, z
              print(t)
    2. Unpacking - Taking values out of collection and assiging to different variables.
        # Tuple - supports packing and unpacking
        # list - supports only unpacking
        # set - packing and unpacking not allowed

6. Tuple is Hasble beacuse it is immutable
    list and set are not hashable but they can be used as values in dictionary

# How to change elements in tuple
    1. convert tuple to list
    2. use list add and delete methods
    3. again convert list to tuple