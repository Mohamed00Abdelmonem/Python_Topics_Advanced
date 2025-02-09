
'''
Problem: Vehicle Types

You need to create a program that models different types of vehicles.
 Each vehicle has a name, number of wheels, and maximum speed. 
 Different types of vehicles will have different numbers of wheels and speeds.
Your task is to create a base class Vehicle and then create subclasses 
for different types of vehicles like Car, Bike, and Truck.
'''


class Vehicle:
    def __init__(self, name, wheels, max_speed):
        self.name = name
        self.wheels = wheels
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.name} has {self.wheels} wheels and can go up to {self.max_speed} mph."
    def info(self):
        print(f"This is {self.name} and it has {self.wheels} wheels and can go up to {self.max_speed} mph.")


class Car(Vehicle):
    def __init__(self, name , wheels, max_speed, color, year_version):
        super().__init__(name, wheels, max_speed)
        self.color = color
        self.year_version = year_version

    def info(self):
        print (f"this is {self.name} and it is {self.color} color and it is {self.year_version} year version")

class Bike(Vehicle):
  pass
class Truck(Vehicle):
    pass
    

car = Car("BMW", 4, 200, "red", 2020)
bike = Bike("Yamaha", 2, 60)
truck = Truck("Volvo", 6, 100)

car.info()
bike.info()
truck.info()