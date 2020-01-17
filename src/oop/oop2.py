# Illustrate How to Create Class Objects with Default Behaviors You Can Override

class GroundVehicle():
    def __init__(self, num_wheels=4):
    # Can set a default value inside the init statementand override for exceptions
        self.num_wheels = num_wheels
    def drive(self):
    # Don't forget you always have to pass "self" in as an argument to Python class methods
        return "vroooom"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        self.num_wheels = num_wheels 
    def drive(self):
        return "BRAAAP!!"

harley = Motorcycle()
chrysler = GroundVehicle()

print(harley.drive())
print(chrysler.drive())

print(harley.num_wheels)
print(chrysler.num_wheels)