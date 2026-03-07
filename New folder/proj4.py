"""
1.warehouse automation system track goods movement,generate reports and process payments
2.CRM(Customer relationship manager)
are customer info ,manage communication logs,and track sales pipelines
3.CRM(Customer relationship manager)
are customer info, manage communication logs and  track sales pipelines 
aar ethe valueis 
"""
#Warehouse automation system 

class Product:
    def __init__(self, pid, name, qty, price):
        self.pid = pid
        self.name = name
        self.qty = qty
        self.price = price

    def add_stock(self, amount):
        self.qty += amount

    def remove_stock(self, amount):
        if amount <= self.qty:
            self.qty -= amount
        else:
            print("Not enough stock")


class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.pid] = product

    def report(self):
        print("\nWarehouse Report")
        for p in self.products.values():
            print(p.pid, p.name, p.qty, p.price)
            print("\t")


class Payment:
    def process(self, product, qty):
        total = product.price * qty
        tax = total * 0.18
        final = total + tax
        print("Total:", final)


p1 = Product(101, "Laptop", 10, 50000)
p2 = Product(102,"Phone",34,75000)
p3 = Product(103,"Earbuds",23,5699)
w = Warehouse()
w.add_product(p1)
w.add_product(p2)
w.report()
w.add_product(p3)
w.report()
pay = Payment()
pay.process(p1, 2)






