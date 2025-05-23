class Teacher:
    def teach(self):
        print("Teaches students")


class MathTeacher(Teacher):
    def math(self):
        print("Solves equations")


class ScienceTeacher(Teacher):
    def science(self):
        print("Conducts experiments")



m = MathTeacher()
m.teach()
m.math()


s = ScienceTeacher()
s.teach()
s.science()

# 🧠 Both MathTeacher and ScienceTeacher inherit from Teacher.

