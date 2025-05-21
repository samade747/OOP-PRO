# ✅ 1. Banking System – Abstracting Transactions

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def transacton(self):
        pass

class Deposit(Bank):
    def transacton(self):
        print("Deposit Transaction")

class Withdraw(Bank):
    def transacton(self):
        print("Withdraw Transaction")

# Create an instance of Deposit and call the transacton method

d = Deposit()
d.transacton()

w = Withdraw()
w.transacton()



# Output: Deposit Transaction
#         Withdraw Transaction


# 🧠 What it teaches:
# Bank is abstract — you can’t use it directly.

# Child classes define how each transaction works.