class BikeShop:
    def __init__(self,stock):
        self.stock = stock

    def ShowBike(self):
        print("Total Bikes :",self.stock)

    def rentBike(self,quantity):

        if quantity <=0:
           print("please enter the positive value or greater than zero")
        elif quantity > self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock - quantity
            print("Total price :",quantity*100)
            print("Total bikes",self.stock)

while True:
    obj = BikeShop(100)
    user_input = int (input("1-> Display stock,2-> rent a bike,3- Exit"))


    if user_input == 1:
        obj.Showbike()
    elif user_input == 2:
        n = int(input("Enter the rent bike :->"))
        obj.rentBike(n)
    else:
            break


        
