# customer relationship manager 


class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.logs = []
        self.stage = "Lead"

    def add_log(self, message):
        self.logs.append(message)

    def update_stage(self, stage):
        self.stage = stage

    def display(self):
        print("\nCustomer Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Sales Stage:", self.stage)
        print("Communication Logs:")
        for log in self.logs:
            print("-", log)


class CRM:
    def __init__(self):
        self.customers = []

    def add_customer(self):
        name = input("Enter customer name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        customer = Customer(name, phone, email)
        self.customers.append(customer)
        print("Customer added successfully!")

    def add_log(self):
        name = input("Enter customer name: ")
        for c in self.customers:
            if c.name == name:
                log = input("Enter communication log: ")
                c.add_log(log)
                print("Log added.")
                return
        print("Customer not found.")

    def update_stage(self):
        name = input("Enter customer name: ")
        for c in self.customers:
            if c.name == name:
                stage = input("Enter new stage (Lead/Proposal/Negotiation/Sale): ")
                c.update_stage(stage)
                print("Stage updated.")
                return
        print("Customer not found.")

    def view_customers(self):
        for c in self.customers:
            c.display()


crm = CRM()

while True:
    print("\n--- CRM System ---")
    print("1. Add Customer")
    print("2. Add Communication Log")
    print("3. Update Sales Stage")
    print("4. View Customers")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        crm.add_customer()
    elif choice == 2:
        crm.add_log()
    elif choice == 3:
        crm.update_stage()
    elif choice == 4:
        crm.view_customers()
    elif choice == 5:
        break
    else:
        print("Invalid choice")