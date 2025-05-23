# ✅ 2. Company Hierarchy – Multilevel Inheritance


class Company:
    def company_info(self):
        print("This is Google Inc.")

class Department(Company):
    def department_info(self):
        print("Works in the AI Department.")

class Employee(Department):
    def employee_info(self):
        print("Employee is a Software Engineer.")

# Usage
e = Employee()
e.company_info()
e.department_info()
e.employee_info()


# 🧠 What it teaches:
# Employee inherits from Department and Company.

