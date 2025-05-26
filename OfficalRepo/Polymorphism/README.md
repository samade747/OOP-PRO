# 🧬 Polymorphism in Python – Real-Life Examples for Beginners

This repository provides 5 beginner-friendly, real-world examples of **Polymorphism in Python**, with code, comments, and explanations — ideal for viva prep (GIAIC), interviews, or just strengthening your OOP skills.

---

## 🧠 What is Polymorphism?

**Polymorphism** means “many forms”.  
It allows the same method or operator to behave differently based on the object or data type.

---

## 📊 Summary Table

| Type                    | Example Covered                  | Description                         |
|-------------------------|----------------------------------|-------------------------------------|
| Duck Typing             | Dog & Cat `speak()`              | Behavior-based flexibility          |
| Method Overriding       | `Bike.start()` vs `Car.start()` | Child redefines parent's method     |
| Operator Overloading    | `+` on int/str/list              | Same operator, different result     |
| Class & Function Poly   | `Shape.area()` in Circle/Rect   | Interface-based behavior change     |
| Abstract Poly           | `Device.operate()`              | Enforced via `abc` module           |

---

## ✅ Real-Life Python Examples

### 1. 🐶 Duck Typing

```python
class Dog:
    def speak(self): print("Bark!")

class Cat:
    def speak(self): print("Meow!")

def sound(animal):
    animal.speak()

sound(Dog())  # Bark!
sound(Cat())  # Meow!


2. 🏍️ Method Overriding

class Vehicle:
    def start(self): print("Generic start.")

class Bike(Vehicle):
    def start(self): print("Kickstart bike.")

class Car(Vehicle):
    def start(self): print("Push start car.")

Bike().start()
Car().start()


3. ➕ Operator Overloading

print(5 + 5)           # 10
print("5" + "5")       # 55
print([1,2] + [3,4])   # [1, 2, 3, 4]


4. 🟦 Shape Area – Function/Class Polymorphism

class Shape:
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * 4 * 4

class Rectangle(Shape):
    def area(self): return 5 * 10

def print_area(shape):
    print("Area:", shape.area())

print_area(Circle())
print_area(Rectangle())
  

5. 🖥️ Abstract Polymorphism

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def operate(self): pass

class Laptop(Device):
    def operate(self): print("Typing...")

class Phone(Device):
    def operate(self): print("Calling...")

Laptop().operate()  # Typing...
Phone().operate()   # Calling...







