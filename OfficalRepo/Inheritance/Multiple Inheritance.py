class Mother:
    def care(self):
        print("Mother cares")

class Father:
    def protect(self):
        print("Father protects")



class Child(Mother, Father):
    def play(self):
        print("Child plays")


c = Child()
c.care()
c.protect()
c.play()

# 🧠 Child inherited from both Mother and Father.