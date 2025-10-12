#1) to print the pattern using for loop
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(end="\n")

#2) to print the pattern using for loop
#1
#23
#456
#78910

num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()

#3) to print the pattern using for loop
# 1 
# 1 0 
# 1 0 1 
# 1 0 1 0
# 1 0 1 0 1

for i in range(1,6):
    for j in range(1, i+1):
        if j%2!=0: 
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

#4) to print the pattern using for loop
# 1 
# 0 0 
# 1 1 1 
# 0 0 0 0
# 1 1 1 1 1

for i in range(1, 6):
    for j in range(i+1):
        if i%2!=0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

#5) to print the pattern using for loop
#         *
#       * *
#     * * *
#   * * * *
# * * * * * 

for i in range(1, 6):
    for j in range(5-i):
        print(" ", end=" ")
    
    for k in range(i):
        print("*",end=" ")
    print()

#6) to print the pattern using for loop(diamond)
#    *  
#  *  * 
# *  *  *
#  *  * 

n = 3
for i in range(1, n+1):
    print("  "*(n-i) + "*  "*i)


#7) to print the pattern using for loop
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# **      **
# ***    ***
# ****  ****
# **********

#upper pattern
for i in range(5, 0, -1):
    print("*"*i +" "*(2*(5-i))+ "*"*i)
#lower patter
for i in range(1, 6):
    print("*"*i +" "*(2*(5-i))+ "*"*i)

#8) to print the pattern using for loop
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

#upper part
for i in range(1,6):
    print("*"*i +" "*(2*(5-i))+ "*"*i)

#lower part
for i in range(4,0,-1):
    print("*"*i +" "*(2*(5-i))+ "*"*i)