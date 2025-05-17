class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def say_hi_to_user(self, user):
    print(f"Hi {user.username}, welcome to our platform!"
    it's {self.username} and I am here to assist you with your orders.
    )
        

user1 = User("samad", "r@r.com", "123456")



print(user1.username)

# Modifying the object data
user1.email = "danny@gmail.com"

print(user1.email)