#  Course 3 ###########################################################################################################

# Let's do an example of class to price european options with the Black and Scholes Model.

from scipy.stats import norm  # For the log normal function
import math
import numpy as np


# Black and Scholes method to price european option

class Bs:
    def __init__(self, typ, r, vol, t, mu, k, s0):
        if typ:
            self.typ = 1  # Case if it is a call
        else:
            self.typ = -1  # Case if it is a put
        self.r = r
        self.vol = vol
        self.T = t
        self.mu = mu
        self.k = k
        self.S0 = s0
        self.pricing()


    def pricing(self):
        self.price = self.typ * (
                    self.S0 * norm.cdf(self.typ * self.d1()) - self.k * math.exp(-self.r * self.T) * norm.cdf(
                self.typ * self.d2()))

    def d1(self):
        return (np.log(self.S0 / self.k) + (self.r + self.vol ** 2 / 2) * self.T) / (self.vol * (self.T)**0.5)

    def d2(self):
        return self.d1() - self.vol * (self.T)**0.5


r = 0.01  # Risk free
vol = 0.1  # Volatility (risk)
T = 10  # Time to maturity, in years
mu = 0.1  # Mean return
k = 100  # strike
S0 = 100  # Current price of the underlying asset


# Creat an object of the class Bs with the inputs given and for a Call
Mypricer1 = Bs(True, r, vol, T, mu, k, S0)

CallPrice = Mypricer1.price  # Save the call price

# Creat an object of the class Bs with the inputs given and for a Put
Mypricer2 = Bs(False, r, vol, T, mu, k, S0)

PutPrice = Mypricer2.price  # Save the put price

# For european options with the same underlying asset, the same strike and the maturity, we can find the price of the
# put if we have the price of the call and vice versa thank to the Call-Put parity :
if round((CallPrice - PutPrice),3) == round(S0 - k * math.exp(-r * T),3):  # we used round(..,3) to have only 3 decimals
    print("The prices of the european put and the european call with the same maturity, the same strike and "
          "the same underlying asset respect the Put-Call parity ")
else:
    print('There is a mistake in the pricer')


# One of the main concept of OOP is inheritance (héritage in french)
# A child class can inherits the informations/structures of the mother class (called also base class)


# Let's use the class Car as mother class
class Car:
    Type = "This is a car"

    def __init__(self, color="Blue"):
        self.color = color

    def driving(self):
        print("The {} car is driving".format(self.color))

    def make_noise(self):
        print("Broummm")


# Let's define ElectricCar as child class
class ElectricCar(Car):  # We have to write the name of the mother class inside the brackets.
    def __init__(self):
        super().__init__("Yellow")  # Use this form, inside the brackets put the parameters.

    def sum_up(self):  # You can define other methods
        print("The car is", self.color, " and this is an electric car")

    def make_noise(self):
        print("No noise")


Tesla = ElectricCar()  # We define the object Tesla of the class ElectricCar (a child class)

Tesla.sum_up()  # We can use the method sum_up from the child class
Tesla.driving()  # We can use the method driving from the mother class
print(Tesla.color)  # We can use the instance attribute from the mother class
print(Tesla.Type)  # We can use the class attribute from the mother class

# make_noise() is an instance method presents in the child class and in the base class. If you call this method
# with the object Tesla, it will call the class method from the child class. We call this processus: overriding.
# So the method make_noise had been overridden.
# Let's try:

Tesla.make_noise()

# Polymorphism #########################################################################################################

'''
This is one of the maine concept of OOP
Polymorphism means many forms 
We use polymorphism : 
_ when we override a method in inheritance (a method in the child class can have the same name has one method in the 
mother class but with different behave) 
_ when we use the same name for different objects like below : 

'''


class Spain:
    @staticmethod
    def capital():
        return "Madrid"


class Italy:
    @staticmethod
    def capital():
        return "Roma"


for country in (Spain, Italy):
    print(country.capital())

'''
 We used staticmethods
 This method can be used without instanciate the class. So we can use this function outside of the class and we don't
 write self inside the brackets. 
 We also write the decorator @staticmethod before def ...(): 
'''


# ex :

class Person:

    def __init__(self, name):
        self.name = name
        self.speaking()
        self.running()

    def speaking(self):
        return "My name is ", self.name

    @staticmethod
    def walking():
        print('I am walking')

    @staticmethod
    def running():
        print('I am running')


# You can call a staticmethod outside the class without instantiation
Person.walking()

# or directly in the init method
Luc = Person("Luc")
