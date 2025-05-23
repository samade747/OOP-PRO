# ✅ 5. Method Overriding in Inheritance

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is moving fast")


c = Car()
c.move()  # Outputs: Car is moving fast


# 🧠 Car overrides the move() method of Vehicle.


# 🧱 Summary Chart: Inheritance in Python

# | Concept               | Description                           |
# | --------------------- | ------------------------------------- |
# | `class Child(Parent)` | Inherits from another class           |
# | `super()`             | Calls parent class method in child    |
# | `pass`                | Use if child doesn’t add anything new |
# | `overriding`          | Child replaces parent method          |
