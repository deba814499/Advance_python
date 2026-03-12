# Custom Exceptions
class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

class DuplicateProductError(Exception):
    pass


class Inventory:
    def __init__(self):
        self.products = {}

    # Add Product
    def add_product(self, product_id, name, quantity):
        if product_id in self.products:
            raise DuplicateProductError("Product ID already exists")

        self.products[product_id] = {
            "name": name,
            "quantity": quantity
        }

        print("Product added successfully")

    # Purchase Product
    def purchase_product(self, product_id, quantity):
        if product_id not in self.products:
            raise InvalidProductIDError("Invalid Product ID")

        if self.products[product_id]["quantity"] < quantity:
            raise OutOfStockError("Not enough stock available")

        self.products[product_id]["quantity"] -= quantity
        print(" Purchase successful")

    # Display Inventory
    def display_inventory(self):
        print("\nInventory List")
        for pid, details in self.products.items():
            print(f"ID: {pid}, Name: {details['name']}, Stock: {details['quantity']}")


# Main Program
inv = Inventory()

try:
    inv.add_product(101, "Laptop", 5)
    inv.add_product(102, "Mouse", 10)

    inv.purchase_product(101, 2)
    inv.purchase_product(103, 1)  # Invalid product

except DuplicateProductError as e:
    print("Error:", e)

except InvalidProductIDError as e:
    print("Error:", e)

except OutOfStockError as e:
    print("Error:", e)

inv.display_inventory()