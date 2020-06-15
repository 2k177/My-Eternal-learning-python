class Vehicle:
    def __init__(self,n,c):
        self.color = c
        self.name = n

    def typeOf(self):
        if self.name=="car":
            print "{} can be driven fastly".format(self.name)
        elif self.name=="Bike":
            print "Ram likes to ride {}".format(self.name)

    def speedof(self):
        if self.color=="red":
            print "speed of {} colored {} is above 220km/h".format(self.color,self.name)
        elif self.color=="Black":
            print "Speed of {} colored {} is below 220km/h".format(self.color,self.name)

if __name__=='__main__':
    car = Vehicle("car", "red")
    car.typeOf()
    car.speedof()
    bike = Vehicle("Bike", "Black")
    bike.speedof()
    bike.typeOf()
