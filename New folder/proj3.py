class BillingSystem:

    def __init__(self):
        self.products = {
            "milk": 50,
            "bread": 30,
            "eggs": 60,
            "rice": 80
        }

        self.cart = []
    def add_product(self):
        item = input("Enter product name: ").lower()

        if item in self.products:
            qty = int(input("Enter quantity: "))
            price = self.products[item] * qty
            self.cart.append(price)
        else:
            print("Product not available")

    def generate_bill(self):
        total = sum(self.cart)
        discount = total * 0.1
        final = total - discount

        print("Total:", total)
        print("Discount:", discount)
        print("Final Amount:", final)


b = BillingSystem()

while True:
    print("\nBilling System")
    print("1.Add Product")
    print("2.Generate Bill")
    print("3.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        b.add_product()
    elif choice == 2:
        b.generate_bill()
    elif choice == 3:
        break