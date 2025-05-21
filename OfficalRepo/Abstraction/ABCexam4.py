# ✅ 4. Payment System – Abstracting Payment Methods

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Usage
credit = CreditCard()
credit.pay(500)

upi = UPI()
upi.pay(250)

# 🧠 What it teaches:
# User calls pay() without worrying about how it’s done.