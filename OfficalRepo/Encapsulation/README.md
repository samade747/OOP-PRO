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
