# ✅ 5. Smart Home – Abstracting Devices

from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is now ON.")


class SmartTV(SmartDevice):
    def turn_on(self):
        print("Smart TV is now ON.")


# Usage
light = SmartLight()
light.turn_on()

tv = SmartTV()
tv.turn_on()


# 🧠 What it teaches:
# One command (turn_on) can work for different smart devices.



# 🔚 Final Thought:
# Abstraction helps developers build systems that are easy to use and hard to misuse, by forcing them to 
# # follow a structure without exposing messy internal details.