# class Vehicle:
#     vehicle_type = "Car" # Class variable or static Variable
    
#     def __init__(self, brand):
#         # Instance variables
#         self.brand = brand
    
#     def get_vehicle_info(self):
#         return f"Brand: {self.brand}, : Type: {Vehicle.vehicle_type}"

# class Engine:
#     engine_type = "V8"
    
#     def __init__(self, horsepower, vehicle):
#         self.horsepower = horsepower
#         self.vehicle = vehicle # Relationship Between Vehicle and Engine

#     def get_engine_info(self):
#         # Accessing class variable of Vehicle using self.vehicle (instance of Vehicle)
#         vehicle_info = self.vehicle.get_vehicle_info()  
#         return f"{vehicle_info}, Engine Type: {Engine.engine_type}, Horsepower: {self.horsepower}"

# car = Vehicle(brand="Toyota")
# engine = Engine(horsepower=150, vehicle=car)# Create an instance of Engine with a reference to Vehicle
# print(engine.get_engine_info())


import pytest




def test_our_test():
    assert 1 == 1

@pytest.mark.skip
def test_should_skipped():
    assert 1 == 1

@pytest.mark.skipif(4>1, reason="skipped 4 > 1")
def test_should_skipped():
    assert 1 == 1

@pytest.mark.xfail
def test_dont_care_if_it_fails():
    assert 1 == 1