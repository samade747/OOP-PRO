# ✅ Example 4: Car Speed Control
# 🚗 Limit speed using encapsulation

class Car:
    def __init__(self):
        self.__speed = 0

    def accelerate(self, value):
        if self.__speed + value <= 180:
           self.__speed += value  # only allow speed up to 180


    def get_speed(self):
        return self.__speed
    
my_car = Car()
my_car.accelerate(150)
print("Current speed:", my_car.get_speed())  # ✅ Output: Current speed: 150
# 🧠 Why encapsulation? Prevent illegal speeds and protect the car’s logic.