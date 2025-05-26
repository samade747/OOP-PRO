# 🧬 What is Polymorphism in Python?
# 📌 Definition:
# Polymorphism means "many forms". In Python OOP, polymorphism allows the same method name to behave differently based on the object calling it.

# It enables:

# Code reusability

# Flexibility

# Cleaner interfaces

# 🚦 Real-Life Analogy

# Think of the word drive():

# A car drives on roads

# A boat drives on water

# A drone drives in the air

# They all "drive", but they do it differently. That’s polymorphism.

# 🛠️ Types of Polymorphism in Python

# | Type                     | Description                                                                                           |
# | ------------------------ | ----------------------------------------------------------------------------------------------------- |
# | **Duck Typing**          | Python cares about behavior, not object type                                                          |
# | **Operator Overloading** | Same operator behaves differently for different types                                                 |
# | **Method Overriding**    | Child class redefines a method from parent class                                                      |
# | **Function Overloading** | Achieved using default arguments or `*args` (Python doesn't support traditional function overloading) |


# ✅ 1. Duck Typing (Behavior-based)

class Dog:
    def speak(self):
        print("Bark!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()  # doesn't care if it's Dog or Cat


dog = Dog()
cat = Cat()


animal_sound(dog)  # Bark!
animal_sound(cat)  # Meow!

# 🧠 Explanation:
# Python doesn’t care if it's a Dog or Cat — if it has a speak() method, it works. This is duck typing: “If it quacks like a duck, it’s a duck.”



# ✅ 2. Method Overriding (Runtime Polymorphism)


class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Bike(Vehicle):
    def start(self):
        print("Kick start the bike.")


class Car(Vehicle):
    def start(self):
        print("Push button start the car.")

v1 = Bike()
v2 = Car()

v1.start()  # Kick start the bike.
v2.start()  # Push button start the car.

# 🧠 Explanation:
# Both Bike and Car override the start() method 
# of the Vehicle class — this is classic method overriding (polymorphism at runtime).


# ✅ 3. Operator Overloading


# print(5 + 10)         # 15 (adds numbers)
# print("5" + "10")     # "510" (concatenates strings)
# print([1, 2] + [3, 4]) # [1, 2, 3, 4] (joins lists)

# 🧠 Explanation:
# The + operator behaves differently based on the operands.
#  This is operator overloading, a form of polymorphism.


# ✅ 4. Polymorphism with Functions and Classes

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 5 * 10

class Circle(Shape):
    def area(self):
        return 3.14 * 4 * 4

def print_area(shape):
    print("Area is:", shape.area())

print_area(Rectangle())  # Area is: 50
print_area(Circle())     # Area is: 50.24

# 🧠 Explanation:
# The function print_area() works with any class that implements area() 
# — showing polymorphism in functions and classes.


# ✅ 5. Polymorphism Using Abstract Base Class

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def operate(self):
        pass

class Laptop(Device):
    def operate(self):
        print("Typing code...")

class Phone(Device):
    def operate(self):
        print("Making a call...")

def use_device(device):
    device.operate()

use_device(Laptop())  # Typing code...
use_device(Phone())   # Making a call...


# 🧠 Explanation:
# Device is an abstract class with an abstract method operate().
# Child classes define their own versions — a great example of runtime polymorphism using abstraction.


# 📌 Summary Chart

# | Type                        | Example                         | Key Feature                        |
# | --------------------------- | ------------------------------- | ---------------------------------- |
# | Duck Typing                 | `animal.speak()` on Dog/Cat     | Python ignores type, uses behavior |
# | Method Overriding           | `Bike.start()` vs `Car.start()` | Child redefines parent method      |
# | Operator Overloading        | `+` on int, str, list           | Same operator, different actions   |
# | Function/Class Polymorphism | `print_area(shape)`             | Same interface, different behavior |
# | Abstract Polymorphism       | `Device.operate()`              | Enforced by abstract base class    |
