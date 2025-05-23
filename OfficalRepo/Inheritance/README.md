# 🧬 Inheritance in Python – Real-Life Examples for Beginners

This repository contains 5 beginner-friendly, real-world examples of **Inheritance in Python**, explained with simple code and clear comments. It's perfect for those preparing for interviews, GIAIC viva, or learning Object-Oriented Programming (OOP).

---

## 📘 What is Inheritance?

Inheritance allows a class (called the **child** or **subclass**) to access the attributes and methods of another class (called the **parent** or **superclass**). It promotes:

- ✅ Code reusability
- ✅ Cleaner structure
- ✅ Easier maintenance

---

## 🔄 Types of Inheritance Covered

| Type                 | Description                          | Example Covered                   |
|----------------------|--------------------------------------|------------------------------------|
| Single Inheritance   | One child inherits from one parent   | University → Student               |
| Multilevel Inheritance | Chain of inheritance                | Company → Department → Employee    |
| Multiple Inheritance | Child inherits from multiple parents | Light + Fan → SmartSwitch          |
| Hierarchical Inheritance | Multiple children from one parent | Staff → Teacher, Clerk             |
| Method Overriding    | Child redefines a parent method      | Transport → Train                  |

---

## ✅ Real-Life Python Examples & Code Description

### 1. 🏫 University System (Single Inheritance)

```python
class University:
    def campus(self):
        print("This university has a beautiful campus.")

class Student(University):
    def study(self):
        print("Student is studying in the university.")
