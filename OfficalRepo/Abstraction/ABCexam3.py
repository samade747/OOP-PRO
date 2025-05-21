# ✅ 3. Vehicle – Abstracting Transportation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key.")


class ElectricScooter(Vehicle):
    def start_engine(self):
        print("Electric scooter started with button.")


# Usage
c = Car()
c.start_engine()

s = ElectricScooter()
s.start_engine()


# 🧠 What it teaches:
# Same interface (start_engine) but different behaviors.

# Abstraction hides how each vehicle works.