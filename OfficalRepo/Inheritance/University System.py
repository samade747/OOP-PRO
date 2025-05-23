✅ 1. University System – Single Inheritance


class University:
    def campus(self):
        print("This university has a beautiful campus.")

class Student(University):
    def study(self):
        print("Student is studying in the university.")

# Usage
s = Student()
s.campus()  # Inherited from University
s.study()


# 🧠 What it teaches:
# Student inherits the campus() method from University.


