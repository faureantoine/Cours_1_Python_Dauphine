# Basics things to know in Python ######################################################################################

"""

Python is case-sensitive, so Capital letters have an impact
The indentation is very important contrary to VBA (this is the space before starting your line)
You don't need to declare the type of the variables contrary to VBA (in VBA you need if you are in Option Explicit)
Generally we use the PEP concept to read easier a code, it is just an aesthetic concept, for instance to name a class we
use a capital letter

"""

# To print something on the console :
print("Hello")  # it's a bit like MsgBox in VBA

# To catch an input :
a = input()  # you have to write on the console the value of your input, it's the same logic that InputBox in VBA
# By default, Python catches the input as a string

# Libraries ############################################################################################################
"""

A library is like a tool box, the two more important are Pandas and Numpy. The first one is for data manipulation and 
analysis. The second one is for applying mathematics and logical operations. To use a library you need to write like 
this : 
import ... as ...
The first blank is the name of the library and the second blank is the nickname that you give

"""

import numpy as np
import pandas as pd

# Data Types ###########################################################################################################

''' We give a name of a variable after an equal and finally the value, doesn't need to give the type '''

# For a string :
name = "Nicolas"

# For an integer (without decimal) :
age = 22

# for a float (with decimal, so any real number with a floating-point) :
size = 1.83

print("My name is ", name, "and I am ", age)

# to check the type of variable :
print(type(age))

# A boolean takes two values : True or False
# True is equal to 1 and False is equal to 0
my_boolean = True

print(3 != 4)  # To check if 3 is not equal to 4
print(4 == 5)  # To check if 4 is equal to 5

# List (very important) :
# A list has elemet(s) that are ordered and they don't need to be unique and they are not necessarely from the same type
my_list = []  # it's to creat an empty list
my_list_2 = [1, 1, 5, "Hey"]

print(my_list_2)

my_list_2.append(3)  # it's to add a value at the end of the list

print(my_list_2)

print(my_list_2[1])  # it's to print the second element of the list (the position starts by 0 !!)

print(my_list_2[-1])  # to print the last element

print(my_list_2[:2])  # to print the elements before the third one

print(my_list_2[2:])  # to print the elements after the second one

s = len(my_list_2)  # to know the size of the list

# Tuple
'''
A tuple is ordered but contrary to a list, we can't modified it after the creation (we say that a tuple is not mutable). 
It can contain different type of element like the lists. We can calculate the number of element and call an element by
its position.
'''

myTuple = (1, "Hey")

# Dictionary (very important)
# a dictionary has elements (keys) that are unique and are not ordered (so impossible to call them by their position, 
# except if you use Python 3.7)
# each key has a value
my_dict = {}  # to creat an empty dictionary

my_dict_2 = {"My_first_Key": 1, "My_second_key": myTuple, "Third_key": my_list_2} 
# so for instance the key "My_first_Key" has the value 1. A key is always a string type

print(my_dict_2["My_first_Key"])

my_dict["Name"] = "David"  # to add a key with its value

# Operators and conditions #############################################################################################

if my_list_2[1] == 2:
    print("The second element is equal to 2")
else:
    print("The second element is not equal to 2")

if my_list_2[1] > 1:
    print("inferior to one")
elif my_list_2[1] <= 0:
    print("negative number")
else:
    print("positive number but inferior to 1")

if my_boolean:
    print("the boolean is True")
else:
    print("the boolean is false")

if not my_boolean:
    print("the boolean is False")
else:
    print("the boolean is True")

# Loop #################################################################################################################
for i in my_list_2:
    print(i)

for i in range(0, 10):
    print(i)

for i in range(len(my_list_2)):
    print(my_list_2[i])

# Example with our dictionary

for a_key in my_dict_2.keys():
    print(a_key)

for a_value in my_dict_2.values():
    print(a_value)

for alld in my_dict_2.items():
    print(alld)

# we can use a While Loop :
num = 0

while num < 5:
    num += 1
    print("num", num)


# Above we wrote num +=1, but it is the same thing as num = num + 1, it is just easier to write as we did, it works for some other operators

# Functions ############################################################################################################

# We want to create a function that squared our input (use ** to square) :
def myfunction(my_input):
    return my_input ** 2


print(myfunction(5))


# recursive function is a function that calls itself
# For instance let's try the factorial (very important for interviews) : n!=n*(n-1)*(n-2)*...*1

# The basic way to write it
def factorial_1(n):
    if n > 1:
        return factorial_1(n - 1)
    else:
        return 1


# the second way is better
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


# A recursive function with Fibonacci (very important for interviews)
def fibonacci(n):
    return fibonacci(n - 1) if n > 1 else 1


# The way to take data from an excel file ##############################################################################

df = pd.read_excel('Data.xlsx')
# You have to write the path before the name of the file if it is not saved in the same folder as your Python code

print(df)

# df is a DataFrame, a DataFrame is a table of data from Pandas with columns/rows name
# it is an important thing in Python because we can manage, look, pick and calculate data easily

# We can manage directly the data :
df.set_index('Date', inplace=True)  # We put the Date column in index

# We can calculate the data :
returns = df.pct_change()  # let's calculate the returns of each column (asset)

VL = (1 + returns).cumprod()  # let's calculate the VL for each column (asset)

# We can pick/change data easily with the position :
VL.iloc[0, :] = 1  # we change the value of the first row (the row zero , and ":" represent all the columns")
# Like in VBA, the first index is for row and the second is for column

# Exception handling ###################################################################################################

try:
    a = 3
    b = 0
    print(a / b)
except:
    print("Error")

print("even if there is and error, the program continues")

try:
    a = "g"
    b = 3
    print(a / b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero not allowed')
