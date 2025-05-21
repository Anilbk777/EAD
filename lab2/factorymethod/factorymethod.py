

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"{self.name} Vehicle"


class Car(Vehicle):
    def __str__(self):
        return f"{self.name} Car"


class Bike(Vehicle):
    def __str__(self):
        return f"{self.name} Bike"


class VehicleFactory:
    def create_vehicle(self, vehicle_type, name):
        if vehicle_type == "car":
            return Car(name)
        elif vehicle_type == "bike":
            return Bike(name)
        else:
            return Vehicle(name)



if __name__ == "__main__":
    factory = VehicleFactory()
    
    my_car = factory.create_vehicle("car", "Toyota")
    print(my_car) 

    my_bike = factory.create_vehicle("bike", "Honda")
    print(my_bike) 
    
    my_vehicle = factory.create_vehicle("unknown", "Generic")
    print(my_vehicle)  