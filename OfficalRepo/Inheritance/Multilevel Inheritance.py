✅ 2. Multilevel Inheritance

class Grandfather:
    def heritage(self):
        print("We have family land.")


class Father(Grandfather):
    def guidance(self):
        print("Father gives advice.")


class Son(Father):
    def dreams(self):
        print("Son wants to innovate.")


s = Son()
s.heritage()
s.guidance()
s.dreams()
# 🧠 Son inherited methods from Father and Grandfather.