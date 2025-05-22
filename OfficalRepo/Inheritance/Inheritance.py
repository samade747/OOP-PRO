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
