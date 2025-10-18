class flipcart:
    def __init__(self):
        self.items = []

    def add_item(self,item_name,qty):
        item = (item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):

        for item in self.items:
            if item[0] ==item_name:
                self.items.remove(item)
                break
    def calculate_total(self):
        total = 0
        for item in self.items:
            total +=item[1]
        return total
# driver code
cart = flipcart()
cart.add_item("Papaya",100)
cart.add_item("Orange",200)
cart.add_item("Guvva",150)

print("Current items in cart : ")
for items in cart.items:
    print(items[0],"-",items[1])

total_qty = cart.calculate_total()
print("Total quantity :",total_qty)

cart.remove_item("Guvva")
print("\n Updated items in cart after removing orange : ")
for item in cart.items:
  print(item[0],"-",item[1])
total_qty = cart.calculate_total()
print("Total quantity : ",total_qty)




















      
