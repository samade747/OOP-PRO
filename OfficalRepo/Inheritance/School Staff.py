# ✅ 4. School Staff – Hierarchical Inheritance


class Staff:
    def work(self):
        print("Staff performs administrative duties.")


class Teacher(Staff):
    def teach(self):
        print("Teacher teaches subjects.")


class Clerk(Staff):
    def maintain_records(self):
        print("Clerk maintains school records.")



# Usage
t = Teacher()
t.work()
t.teach()

c = Clerk()
c.work()
c.maintain_records()


# 🧠 What it teaches:
# Teacher and Clerk both inherit from Staff.