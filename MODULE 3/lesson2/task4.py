from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass
class Car(Vehicle):
    def create(self):
        return "Car created"

class Bike(Vehicle):
    def create(self):
        return "Bike created"
    

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "Car":
            return Car()
        elif vehicle_type == "Bike":
            return Bike()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


if __name__ == "__main__":
    factory = VehicleFactory()
    
    car = factory.create_vehicle("Car")
    print(car.create())  
    
    bike = factory.create_vehicle("Bike")
    print(bike.create())