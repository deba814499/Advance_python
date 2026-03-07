#password manager curely store ,add,edit,and retrieve user passwords using encryption

import base64

class PasswordManager:

    def __init__(self):
        self.passwords = {}

    # Encrypt password
    def encrypt(self, password):
        encoded = base64.b64encode(password.encode()).decode()
        return encoded

    # Decrypt password
    def decrypt(self, encrypted):
        decoded = base64.b64decode(encrypted.encode()).decode()
        return decoded

    # Add new password
    def add_password(self, site, password):
        self.passwords[site] = self.encrypt(password)
        print("Password added successfully")

    # Edit password
    def edit_password(self, site, new_password):
        if site in self.passwords:
            self.passwords[site] = self.encrypt(new_password)
            print("Password updated")
        else:
            print("Site not found")

    # Retrieve password
    def get_password(self, site):
        if site in self.passwords:
            print("Password:", self.decrypt(self.passwords[site]))
        else:
            print("Site not found")

    # View stored sites
    def view_sites(self):
        print("Stored Accounts:")
        for site in self.passwords:
            print(site)


pm = PasswordManager()

while True:
    print("\nPassword Manager")
    print("1. Add Password")
    print("2. Edit Password")
    print("3. Retrieve Password")
    print("4. View Sites")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        site = input("Enter site name: ")
        password = input("Enter password: ")
        pm.add_password(site, password)

    elif choice == "2":
        site = input("Enter site name: ")
        new_password = input("Enter new password: ")
        pm.edit_password(site, new_password)

    elif choice == "3":
        site = input("Enter site name: ")
        pm.get_password(site)

    elif choice == "4":
        pm.view_sites()

    elif choice == "5":
        break