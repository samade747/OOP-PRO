# ✅ 1. University System – Single Inheritance

class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.sound()  # From Animal
d.bark()   # From Dog



🧠 Dog inherited the sound() method from Animal.