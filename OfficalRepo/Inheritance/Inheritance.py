# 🧠 What is Inheritance in Python?
# Inheritance allows one class (child) to reuse the properties and methods of another class (parent).

# Think of it like:
# 👨‍👩‍👧 Child inherits traits (like eyes or habits) from parents — the same way a class inherits behavior from another.



# ✅ Why use Inheritance?
# | Feature          | Benefit                          |
# | ---------------- | -------------------------------- |
# | Code Reusability | Don’t repeat code in every class |
# | Structure        | Models real-world relationships  |
# | Scalability      | Easy to expand and maintain code |


# 📘 Basic Syntax

class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    pass

c = Child()
c.speak()  # Inherited from Parent


# 🔍 Types of Inheritance in Python

# | Type         | Example                           |
# | ------------ | --------------------------------- |
# | Single       | One child from one parent         |
# | Multilevel   | Grandchild inherits from child    |
# | Multiple     | One child from multiple parents   |
# | Hierarchical | Multiple children from one parent |



# ✅ 1. Single Inheritance

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()  # From Animal
d.bark()   # From Dog



# ✅ 2. Multilevel Inheritance

class Grandfather:
    def heritage(self):
        print("We have family land.")

class Father(Grandfather):
    def guidance(self):
        print("Father gives advice.")

class Son(Father):
    def dreams(self):
        print("Son wants to innovate.")


s = Son()
s.heritage()
s.guidance()
s.dreams()

# 🧠 Son inherited methods from Father and Grandfather.

# ✅ 3. Multiple Inheritance

class Mother:
    def care(self):
        print("Mother cares")

class Father:
    def protect(self):
        print("Father protects")

class Child(Mother, Father):
    def play(self):
        print("Child plays")

c = Child()
c.care()
c.protect()
c.play()


# 🧠 Child inherited from both Mother and Father.


# ✅ 4. Hierarchical Inheritance

class Teacher:
    def teach(self):
        print("Teaches students")

class MathTeacher(Teacher):
    def math(self):
        print("Solves equations")

class ScienceTeacher(Teacher):
    def science(self):
        print("Conducts experiments")

m = MathTeacher()
m.teach()
m.math()

s = ScienceTeacher()
s.teach()
s.science()
# 🧠 Both MathTeacher and ScienceTeacher inherit from Teacher.

# ✅ 5. Method Overriding in Inheritance
# Child class can override a parent method:


class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is moving fast")

c = Car()
c.move()  # Outputs: Car is moving fast

# 🧠 Car overrides the move() method of Vehicle.

# | Concept               | Description                           |
# | --------------------- | ------------------------------------- |
# | `class Child(Parent)` | Inherits from another class           |
# | `super()`             | Calls parent class method in child    |
# | `pass`                | Use if child doesn’t add anything new |
# | `overriding`          | Child replaces parent method          |

