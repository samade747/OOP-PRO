# ✅ 3. Appliance Control – Multiple Inheritance


class Light:
    def turn_on_light(self):
        print("Light turned on.")


class Fan:
    def turn_on_fan(self):
        print("Fan turned on.")


class SmartSwitch(Light, Fan):
    def status(self):
        print("Smart Switch is operational.")

# Usage
switch = SmartSwitch()
switch.turn_on_light()
switch.turn_on_fan()
switch.status()


# 🧠 What it teaches:
# SmartSwitch can control both light and fan, inheriting from both.

