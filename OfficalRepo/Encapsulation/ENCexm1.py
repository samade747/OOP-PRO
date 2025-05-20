# ✅ Example 1: Bank Account
# 🔒 Encapsulating balance to protect it from direct access

class BankAccount:
    def __init__(self):
        self.__balance = 0 # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount # Modifying private variable


    def get_balance(self):
        return self.__balance # Getter Method
    

account = BankAccount()
account.deposit(1000)
print(account.get_balance())  # ✅ Output: 1000
# 🧠 Why encapsulation? We don’t want anyone to directly change __balance to a negative number.

