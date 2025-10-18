class ShoppingCart:
    """
    A simplified class to manage items and calculate the total price.
    Items are stored as a list of dictionaries.
    """
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int = 1):
        """Adds a new item or increases the quantity of an existing one."""
        
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                print(f"Updated: Added {quantity} x {name}. New quantity: {item['quantity']}")
                return 
        
        new_item = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.items.append(new_item)
        print(f"Added: {quantity} x {name} at ${price:.2f}.")

    def remove_item(self, name: str, quantity: int = 1):
        """Removes a specified quantity of an item."""
        
        item_to_remove = None
        for item in self.items:
            if item['name'] == name:
                item_to_remove = item
                break
        
        if not item_to_remove:
            print(f"Error: Item '{name}' is not in the cart.")
            return

        current_qty = item_to_remove['quantity']
        
        if quantity >= current_qty:
            
            self.items.remove(item_to_remove)
            print(f"Removed ALL ({current_qty}) units of {name}.")
        else:
            
            item_to_remove['quantity'] -= quantity
            print(f"Removed {quantity} x {name}. Remaining: {item_to_remove['quantity']}.")


    def calculate_total(self) -> float:
        """Calculates the total cost of all items in the cart."""
        total = 0.0
        for item in self.items:
            total += item['price'] * item['quantity']
        
        return round(total, 2)

    def display_cart(self):
        """Prints a user-friendly summary of the cart."""
        if not self.items:
            print("\n--- The shopping cart is empty ---")
            return

        print("\n--- Current Shopping Cart ---")
        for item in self.items:
            subtotal = item['price'] * item['quantity']
            print(f"  - {item['name']} (x{item['quantity']}): ${item['price']:.2f} each | Subtotal: ${subtotal:.2f}")
        
        print("-----------------------------")
        print(f"GRAND TOTAL: ${self.calculate_total():.2f}")
        print("-----------------------------")
