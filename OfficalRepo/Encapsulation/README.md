✅ What is Encapsulation in Python?
Encapsulation means hiding the internal details of how something works and only exposing what’s necessary.

Just like:

A TV remote hides complex circuits and gives you only buttons to control.

A car hides the engine, and you use the steering wheel and pedals to drive.

✅ Why is Encapsulation important?
It protects data from being accidentally changed.

Makes code easier to understand and maintain.

Helps enforce rules and security.



✅ How does Encapsulation work in Python?
Python uses classes to support encapsulation.

There are 3 types of access levels for variables and methods:

Access Modifier	Syntax	Meaning
Public	var	Accessible everywhere
Protected	_var	Accessible in class and subclass (by convention)
Private	__var	Hidden from outside access


| Access Type | Declaration   | Accessible From                      |
| ----------- | ------------- | ------------------------------------ |
| Public      | `self.name`   | Anywhere                             |
| Protected   | `self._name`  | Class + Subclasses (suggested only)  |
| Private     | `self.__name` | Only inside the class (name mangled) |



| 🔢 Concept        | 💡 Description                                                              | 🧪 Example Syntax             | 🚦 Access Scope                      |
| ----------------- | --------------------------------------------------------------------------- | ----------------------------- | ------------------------------------ |
| **Encapsulation** | Wrapping data and methods into a single unit (class) and restricting access | `class ClassName:`            | Helps in data protection             |
| **Public**        | Can be accessed from anywhere                                               | `self.name`                   | Everywhere                           |
| **Protected**     | Should not be accessed outside the class (but can be); used by convention   | `self._name`                  | Class + Subclass                     |
| **Private**       | Cannot be accessed directly from outside the class                          | `self.__name`                 | Only inside the class                |
| **Getter Method** | Used to **read** a private/protected variable                               | `def get_name(self):`         | Controlled reading of data           |
| **Setter Method** | Used to **update** a private/protected variable                             | `def set_name(self, value):`  | Controlled writing/modifying of data |
| **Why Use It?**   | - Hide internal data  <br> - Enforce validation  <br> - Improve security    | `self.__balance` with getters | Prevents direct unauthorized access  |




| 💼 Real-Life Example   | 🔒 Protected Data | ✅ Reason for Encapsulation          |
| ---------------------- | ----------------- | ----------------------------------- |
| Bank Account           | `__balance`       | Prevent fraud or incorrect updates  |
| Student Grades         | `__marks`         | Enforce marks range (0–100)         |
| Car Speed Controller   | `__speed`         | Limit speed for safety              |
| Password Manager       | `__password`      | Hide password content               |
| Employee Salary System | `__salary`        | Secure sensitive salary information |

