#Abstract class that can't be instantianted on its own ,has to be sub classed
# They can contain abstract methods , which are declared but have no implementation
# BENEFITS:
#          Prevents instantiation of the class itself
#          Requires children to use inherited abstract methods 
from abc import ABC ,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
         print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")
    def stop(self):
        print("You stop the motorcycle")

class Truck(Vehicle):
    def go(self):
        print("You drive the truck")
    def stop(self):
        print("You stop the truck")

car = Car()
car.stop()
car.go()
truck = Truck()
truck.go()
truck.stop()
