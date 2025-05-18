class Person:
    def __init__(self, name):
       self.name = name    # Public Attribute, Instance Variable
       self.state = "Idle" # Default State


    def running(self):
        self.state = "Runnning"
        print(f"{self.name} is {self.state}")

    def walking(self):
        self.state = "Walking"
        print(f"{self.name} is {self.state}")

    def sleeping(self):
        self.state = "Sleeping"
        print(f"{self.name} is {self.state}")

    def show_state(self):
        print(f"{self.name} is {self.state}")



person = Person("Samad")
person.show_state() # Samad is Idle

person.running() # Samad is Runnning
person.show_state() # Samad is Runnning

person.walking() # Samad is Walking
person.show_state() # Samad is Walking