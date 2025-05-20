# Practice Exercise 
class Animal:
    def __init__(self):
        self._species = "Dog"  # Protected variable


class Pet(Animal):
    def show_species(self):
        print("Pet species is:", self._species)

# Step 1: p = Pet()
# You are creating an object of the Pet class.
# Pet is a child class (subclass) of Animal.
# When you create the Pet object, Python looks for a constructor __init__ in Pet.
# But Pet has no __init__, so it uses the one from its parent class Animal.


# Step 2: p.show_species()
# This calls the show_species() method of the Pet class.
# Inside it, you have:



p = Pet()
p.show_species()

# self._species accesses the protected variable inherited from the parent class Animal
