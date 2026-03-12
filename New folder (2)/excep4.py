#Ecommerce System with Custom Exceptions

class OutOfStockError(Exception):
    pass

class InvalidCouponError(Exception):
    pass

class InvalidPaymentMethodError(Exception):
    pass

class EcommerceSystem:

    def __init__(self):
        self.products = {
            "Laptop": {"price": 50000, "stock": 5},
            "Phone": {"price": 20000, "stock": 10},
            "Headphones": {"price": 2000, "stock": 15}
        }

        self.valid_coupons = {"SAVE10": 0.10, "SAVE20": 0.20}
        self.payment_methods = ["UPI", "Card", "Cash"]
        self.orders = []
        self.returns = []

    def place_order(self, product, quantity, coupon, payment):

        if product not in self.products:
            print(" Product not found")
            return 

        if self.products[product]["stock"] < quantity:
            raise OutOfStockError("Product is out of stock")

        price = self.products[product]["price"] * quantity

        if coupon:
            if coupon not in self.valid_coupons:
                raise InvalidCouponError("Invalid coupon code")
            discount = price * self.valid_coupons[coupon]
            price -= discount

        if payment not in self.payment_methods:
            raise InvalidPaymentMethodError("Invalid payment method")

        self.products[product]["stock"] -= quantity

        order = {"product": product, "quantity": quantity, "total": price}
        self.orders.append(order)

        print(" Order placed successfully")
        print("Total Amount:", price)
        

    def return_order(self, product, quantity):
        self.products[product]["stock"] += quantity
        print("Return successful. Stock updated.")

    def refund(self, amount):
        print(f" Refund of {amount} processed successfully.")


# Main Program

system = EcommerceSystem()

try:
    system.place_order("Laptop", 2, "SAVE10", "UPI")
except Exception as e:
    print("Error:", e)

try:
    system.place_order("Laptop", 10, "", "Card")
except Exception as e:
    print("Error:", e)

system.return_order("Laptop", 1)
system.refund(45000)