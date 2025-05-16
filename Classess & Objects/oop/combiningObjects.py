class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number



dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")


print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max
print(dog1.breed)  # Output: Golden Retriever
print(dog2.breed)  # Output: Bulldog
dog1.bark()  # Output: Buddy says Woof! 
dog2.bark()  # Output: Max says Woof!



