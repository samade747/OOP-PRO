# ✅ Example 3: Password Manager
# 🔐 Keeping passwords private

class PasswordManager:
    def __init__(self):
        self.__password = "" # Private variable

    def set_password(self, password):
        if len(pwd) >= 8:
            self.__password = password  # Only allow strong passwords

    def get_password(self):
        return "*" * len(self.__password)  # Return masked password
    
pm = PasswordManager()
pm.set_password("mySecert1234")
print("stored Password:", pm.get_password())  # ✅ Output: stored Password: ************
# # 🧠 Why encapsulation? We want to ensure passwords are strong and not easily accessible.