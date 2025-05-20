# ✅ Example 2: Student Marks
# 🎓 Keeping marks safe and controlled

class Student:
    def __init__(self):
        self.__marks = 0 # Private variable

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks  # Only allow valid marks

    def get_marks(self):
        return self.__marks # Getter Method
    
s = Student()
s.set_marks(85)
print("Marks:", s.get_marks())  # ✅ Output: Marks: 85
# # 🧠 Why encapsulation? We want to ensure marks are always between 0 and 100.
