#  Course 2 ############################################################################################################

#  Let's use what we learnt before #####################################################################################

# We have three dictionaries :
Alban = {"Age": 22, "positive Covid test": False, "Symptoms": False}
Lucie = {"Age": 20, "positive Covid test": True, "Symptoms": False}
Julie = {"Age": 18, "positive Covid test": True, "Symptoms": True}

# This is a list containing our dictionaries
people = [Alban, Lucie, Julie]
pos = 0
pos_and_symp = 0

# The loop checks for each element (one element is called "person") of the list "people"
for person in people:
    if person["positive Covid test"]:
        pos += 1
        if person["Symptoms"]:
            pos_and_symp += 1


# pos is the number of positive people and pos_and_symp is the number of positive people with symptoms.

#  Functions Part 2 ####################################################################################################

# We saw how to write a normal function, ex :
def my_function(n):
    return n + 2


print(my_function(4))


# We can define function with default parameters :
def my_function_bis(n, m=2):
    return n + m


# so we can give one or two parameters :
print(my_function_bis(3, 6))
print(my_function_bis(4))


# To know what type of input we have to give we can write like this :
def my_new_function(n: int, m=2):  # So the input that we have to give is an integer
    return n + m


# To know what type of output we will have we can write like this :
def my_new_function(n: int, m=2) -> int:  # So the output is an integer
    return n + m


#  Special functions ###################################################################################################


# Map is useful to apply a function in each element of an iterable
# Iterables are containers that can store multiple values and are capable of returning them one by one (list, tuple, dictionary etc)
# map( function , iterable)

my_iterable = [2, 3, 4, 5]
the_results = map(my_new_function, my_iterable)

# The output is a map object, if you want to transform it into a list use list()
print(list(the_results))


# Filter
# Filter is written like a map function : filter( function, iterable ) 
# Nevertheless the function must return boolean values 
# and the output of the filter function is the element(s) of the iterable that makes the output of the function equals to True. 

def my_function(n): # This function returns True if the input is superior to 2, False otherwise
    return n>2

my_results = list(filter(my_function, [1, 2, 3, 4, 5])) # Don't forget to transform the filter object into a list

print(my_results) # Only the elements of the iterable are shown because the make the output of the function equals to True. 


# Lambda is an anonymous function, so we don't need to give a name to this function
# If a and b our two arguments :

the_funct = lambda a, b: a + b  # For this example the function is not anonymous, it is called the_funct

print(the_funct(2, 7))


# Lambda is used especially for map and filter functions cause it can be used as anomymous function. 


print(list(map(lambda a: a * a, my_iterable)))  # In this example the lambda function a*a is anonymous

print(list(filter(lambda a: a>2, [1, 2, 3, 4, 5])))


#  Class ##############################################################################################################


# OOP (Object Oriented Programming) is a concept for class and objects


# My first (empty) class :
class Car:
    pass


# My first object of the class Car
MyCar = Car()


# Let's add a class attribute
class Car:
    Type = "This is a car"
    pass


MyCar = Car()

# To have access of the class attribute Type outside the class
print(MyCar.Type)


# A class attribute is the same for all the objects of the class Car unless you change it

# Constructors are directly called when you creat an object
class Car:
    Type = "This is a car"

    def __init__(self):
        print("I am inside the constructor")


# Let's try in creating an object of the class Car
MyObject = Car()


# In creating an object the constructor __init__(self): had been called immediately (we call it the init method)


# Instance attributes are like class attribute but it can change from one object to another:
class Car:
    Type = "This is a car"

    def __init__(self, brand, color):
        self.brand = brand  # brand and color are initialized (assign values)
        self.color = color


# We instantiate the object MyCar and HisCar:
MyCar = Car("Toyota", "blue")
HisCar = Car("Tesla", "White")

print(MyCar.Type)
print(MyCar.brand)
print(MyCar.color)

print(HisCar.Type)
print(HisCar.brand)
print(HisCar.color)


# So the class attribute Type is the same for the two objects, but the instance attributes brand and color are different

# Self is like the state of the object, it is used to access variables that belongs to the class.

# Instance method
class Car:

    def __init__(self, color: str):  # the input color must be a string
        self.color = color

    def driving(self):  # this is an instance method
        print("The {} car is driving".format(self.color))  # same as print("The ", self.color, " car is driving")


MyCar = Car("blue")

MyCar.driving()  # We know that driving is a method cause they are brackets


# An instance method can be called directly when we creat an object:
class Car:
    Type = "This is car"

    def __init__(self, brand: str, the_color="Blue"):
        self.color = the_color
        self.brand = brand
        self.driving()

    def driving(self) -> str:
        print("The {} car is driving".format(self.color))


MyCar = Car("Toyota")
'''
So to explain the path of the code :
1) I created the object MyCar of the class Car, with one parameter. We instantiated the object MyCar of the class Car
2) "Type" is saved and this is a class attribute.
3) As a constructor (a constructor is called directly when we instantiate the object), the init method is called 
(__init__(self,...)). The instance attributes color and model are initialized with the value "Blue" and "Toyota". 
"Blue" is the value by default. 
4) We are still inside the constructor and we call the method driving() 
5) We are inside the method driving() and we print the sentence with the instance attribute color 
That's why the sentence "The Blue car is driving" appeared.
'''
