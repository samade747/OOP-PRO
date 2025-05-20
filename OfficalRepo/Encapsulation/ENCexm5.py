# ✅ Example 5: Employee Salary
# 💼 Protecting salary information

class Employee:
    def __init__(self):
        self.__salary = 0 # Private variable

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary  # Only allow positive salary
            # validate salary before setting

    def get_salary(self):
        return self.__salary
    

e = Employee()
e.set_salary(50000)
print("Salary:", e.get_salary())  # ✅ Output: Salary: 50000

🧠 Why encapsulation? Keeps sensitive financial data secure and only allows valid updates.