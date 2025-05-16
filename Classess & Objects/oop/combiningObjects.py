class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f"{self.name} says Woof!")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number



owner1 = Owner("Alice", "123 Main St", "555-1234")
owner2 = Owner("Bob", "456 Elm St", "555-5678")


dog1 = Dog("Buddy", "Golden Retriever", owner1)
dog2 = Dog("Max", "Bulldog", owner2)


print(dog1.name)  # Output: Buddy
print(dog2.name)  # Output: Max
print(dog1.breed)  # Output: Golden Retriever
print(dog2.breed)  # Output: Bulldog
dog1.bark()  # Output: Buddy says Woof! 
dog2.bark()  # Output: Max says Woof!


print(dog1.owner.name)  # Output: Alice
print(dog1.owner.address)  # Output: 123 Main St
print(dog1.owner.contact_number)  # Output: 555-1234

print(dog2.owner.name)  # Output: Bob
print(dog2.owner.address)  # Output: 456 Elm St
print(dog2.owner.contact_number)  # Output: 555-5678
