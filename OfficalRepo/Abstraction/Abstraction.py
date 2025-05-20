# Abstraction means hiding complex implementation details and exposing only the necessary features of an object. It helps reduce complexity and allows the programmer to focus on interactions at a higher level.

# Example:

# You don’t need to know how a car’s engine works to drive it. Similarly, a Car class might expose a drive() method without revealing the internal mechanics.


# 🧠 What is Abstraction?
# Abstraction means showing only the necessary details and hiding the complex parts.

# 📦 Imagine driving a car:

# You press the accelerator, but don’t need to know how the engine works.

# You just use the car’s interface, not its internal system.

# That’s abstraction!

# 🧩 In Python (OOP), abstraction is used to:
# Define what should be done (but not how it's done)

# Hide the implementation details from the user

# Python uses abstract classes and methods to do this.

# 🔧 How to do Abstraction in Python?
# We use:

# ABC → Abstract Base Class

# @abstractmethod → Mark a method that must be implemented in child class

# These come from abc module (built-in).


# | Step | What to Do                              | Why                             |
# | ---- | --------------------------------------- | ------------------------------- |
# | 1    | Import `ABC` and `abstractmethod`       | To create abstract classes      |
# | 2    | Create a class that inherits from `ABC` | This makes it an abstract class |
# | 3    | Use `@abstractmethod` in methods        | These must be implemented later |


# 🎯 Real-Life Example: Payment System
# Let’s build a real-world example step-by-step.


# 🔷 Abstract Class

from abc import ABC, abstractmethod

class Payment(ABC):  # Abstract class
    @abstractmethod
    def make_payment(self, amount):
        pass  # No implementation here

# 🔶 Concrete Class

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using PayPal.")

✅ Using It
p1 = CreditCardPayment()
p1.make_payment(100)  # Output: Paid 100 using Credit Card.

p2 = PayPalPayment()
p2.make_payment(50)  # Output: Paid 50 using PayPal


# 🎯 Why Use Abstraction?


# | Benefit            | Meaning                                    |
# | ------------------ | ------------------------------------------ |
# | Hides complexity   | You don't see how the payment is processed |
# | Code flexibility   | Add more types (e.g., UPI, Crypto) easily  |
# | Enforces structure | All payments must have `make_payment()`    |



# 🔁 Simple Analogy

# | Real World      | Abstraction In Code                       |
# | --------------- | ----------------------------------------- |
# | Car accelerator | You press it, car moves (but how? hidden) |
# | ATM             | You press buttons, money comes out        |
# | TV Remote       | You press power, TV turns on              |

# >>>>>>>>>>>>>>>>>>>>>  new session <<<<<<<<<<<<<<<<<<<<<<<<<<<<


# 🧠 What is Abstraction?
# Abstraction means showing only the necessary details and hiding the complex parts.

# 📦 Imagine driving a car:

# You press the accelerator, but don’t need to know how the engine works.

# You just use the car’s interface, not its internal system.

# That’s abstraction!


# 🧩 In Python (OOP), abstraction is used to:
# Define what should be done (but not how it's done)

# Hide the implementation details from the user

# Python uses abstract classes and methods to do this.



# ✅ Step-by-Step Example
# 🧪 Step 1: Import tools

from abc import ABC, abstractmethod


# 🧪 Step 2: Create an abstract class

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # No implementation here - No body — only structure


# Animal is an abstract class

# make_sound() is an abstract method

# It only defines what should happen, not how


# 🧪 Step 3: Create child classes (that implement the abstract method)


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


# These classes inherit from Animal

# They implement the make_sound method

d = Dog()
d.make_sound()  # Output: Woof!

c = Cat()
c.make_sound()  # Output: Meow!


# 🧱 Why Use Abstraction?
# | Feature                          | Benefit                           |
# | -------------------------------- | --------------------------------- |
# | Hides internal complexity        | Makes code clean and simple       |
# | Focuses on **what**, not **how** | Users don’t see unnecessary logic |
# | Forces structure                 | Helps build large apps with rules |


# ❌ What You Can’t Do
# You can’t create an object of an abstract class directly:


a = Animal()  # ❌ Error! Can't instantiate abstract class
# You must create a child class that implements the abstract method first.


# ✅ Summary
# | Term              | Meaning                                   |
# | ----------------- | ----------------------------------------- |
# | `ABC`             | Abstract Base Class                       |
# | `@abstractmethod` | Method without body — must be overridden  |
# | Abstraction       | Hides logic, shows only required features |
