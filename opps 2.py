class vehicle:
    def describe(self):
        print("This is a generic vehicle.")

class car(vehicle):

    print("This is a sporty car.")

class motorcycle(vehicle):
    def describe(self):
        print("This is a fast motorcycle.")

vehicle = vehicle()
car = car()
motorcycle = motorcycle()
vehicle.describe()
car.describe()
motorcycle.describe()
