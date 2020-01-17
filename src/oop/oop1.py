# Demonstrate Understanding of Python Object Class Hierarchy

# Base/Parent
class Vehicle:
    pass 

# Child
class Starship(Vehicle):
    pass

# Child
class FlightVehicle(Vehicle):
    pass 

# Grandchild
class Airplane(FlightVehicle):
    pass

# Child
class GroundVehicle(Vehicle):
    pass 

# Grandchild
class Car(GroundVehicle):
    pass 

# Grandchild
class Motorcycle(GroundVehicle):
    pass