# ✅ 5. Transport System – Method Overriding

class Transport:
    def travel_mode(self):
        print("General transport method.")


class Train(Transport):
    def travel_mode(self):
        print("Traveling by train on tracks.")


# Usage
t = Train()
t.travel_mode()  # Overridden method

# 🧠 What it teaches:
# Train overrides the parent class method travel_mode.


