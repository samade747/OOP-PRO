# Encapsulation

# Example 1: Public Variable (Anyone can access)
class Student:
    def __init__(self):
        self.name = "John"  # Public

student = Student()
print(student.name)  # ✅ Output: John


# Protected Variables in Python
# In Python, a protected variable is defined with a single underscore: _variable.

# 🧠 This is just a convention, not a strict rule. It suggests that:

# You should not access it outside the class directly.

# But you can access it if needed (unlike private variables).

# Example 2: Protected Variable in a Class

class Person:
    def __init__(self):
        self._name = "Sam"  # Protected variable

p = Person()
print(p._name)  # ✅ You can still access it, but it's not recommended

# This works, but using _name tells other programmers: "Treat this as internal – don’t access it directly."


# Example 2: Accessing Protected Variable in a Subclass

class Person:
    def __init__(self):
        self._name = "Sam"

class Student(Person):
    def print_name(self):
        print("Student name is:", self._name)

s = Student()
s.print_name()  # ✅ Accessing protected member in subclass
# Student name is: Sam
# Protected variables are meant to be accessed
#  inside the class and its child classes (subclasses).





# Example 3: Private Variable (Encapsulated)
class Student:
    def __init__(self):
        self.__name = "John"  # Private

student = Student()
print(student.__name)  # ❌ Error: Cannot access private variable

#  But you can access it using getter and setter methods:



# | Access Type | Declaration   | Accessible From                      |
# | ----------- | ------------- | ------------------------------------ |
# | Public      | `self.name`   | Anywhere                             |
# | Protected   | `self._name`  | Class + Subclasses (suggested only)  |
# | Private     | `self.__name` | Only inside the class (name mangled) |



# | Concept       | Example             | Use                      |
# | ------------- | ------------------- | ------------------------ |
# | Public        | `self.name`         | Accessible anywhere      |
# | Protected     | `self._name`        | Accessible in subclasses |
# | Private       | `self.__name`       | Hidden from outside      |
# | Getter Method | `get_name()`        | To read private data     |
# | Setter Method | `set_name("Alice")` | To update private data   |

