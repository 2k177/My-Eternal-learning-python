class Vehicle:
    def generalProperty(self):
        print "Generic Purpose: It is used for transportation purpose"

class Car(Vehicle):

    def __init__(self):
        print "Am Car"
        self.wheels = 4
        self.roofTop = True
        self.generalProperty()

    def specificProperty(self):
        print "Specific Usage: is used for long drive and family vacation"

class Bike(Vehicle):

    def __init__(self):
        print "Am Bike"
        self.wheels = 2
        self.roofTop = False
        self.generalProperty()

    def specificProperty(self):
        print "Specific Usage: is used for Racing and solo trips"

if __name__=="__main__":
    car = Car()
    car.specificProperty()
    bike = Bike()
    bike.specificProperty()
    print isinstance(car,Car)                               #check if the object is instance of class(Returns True)
    print isinstance(car,Bike)                              #Returns False
    print issubclass(Car, Vehicle)                          #checks if car is subclass of vehicle