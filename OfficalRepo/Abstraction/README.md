🧠 What is Abstraction?
Abstraction means showing only the necessary details and hiding the complex parts.

📦 Imagine driving a car:

You press the accelerator, but don’t need to know how the engine works.

You just use the car’s interface, not its internal system.

That’s abstraction!

🧩 In Python (OOP), abstraction is used to:
Define what should be done (but not how it's done)

Hide the implementation details from the user

Python uses abstract classes and methods to do this.

🔧 How to do Abstraction in Python?
We use:

ABC → Abstract Base Class

@abstractmethod → Mark a method that must be implemented in child class

These come from abc module (built-in).



| Step | What to Do                              | Why                             |
| ---- | --------------------------------------- | ------------------------------- |
| 1    | Import `ABC` and `abstractmethod`       | To create abstract classes      |
| 2    | Create a class that inherits from `ABC` | This makes it an abstract class |
| 3    | Use `@abstractmethod` in methods        | These must be implemented later |

🎯 Real-Life Example: Payment System
Let’s build a real-world example step-by-step.
