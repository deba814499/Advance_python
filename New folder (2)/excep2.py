class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        try:
            
            if not name or not phone:
                raise ValueError("Fields cannot be empty")
                

            if name in self.contacts:
                raise Exception("Contact already exists")

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Phone number must be 10 digits")

            self.contacts[name] = phone
            print("Contact added successfully.")

        except Exception as e:
            print("Error:", e)

    def edit_contact(self, name, phone):
        try:
            if name not in self.contacts:
                raise KeyError("Contact not found")

            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Invalid phone number format")

            self.contacts[name] = phone
            print("Contact updated.")

        except Exception as e:
            print("Error:", e)

    def search_contact(self, name):
        try:
            if name not in self.contacts:
                raise KeyError("Contact not found")

            print("Name:", name)
            print("Phone:", self.contacts[name])

        except Exception as e:
            print("Error:", e)

    def display_contacts(self):
        print("\nContact List")
        for name, phone in self.contacts.items():
            print(name, ":", phone)


book = ContactBook()

book.add_contact("Rahul", "9876543210")
book.add_contact("Amit", "9123456789")
book.search_contact("Rahul")
book.search_contact("Rahul")
book.edit_contact("Rahul", "9999999999")
book.display_contacts()
