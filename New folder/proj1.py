import time

class ParkingLot:
    def __init__(self):
        self.parking = {}

    def vehicle_entry(self):
        vehicle = input("Enter vehicle number: ")
        self.parking[vehicle] = time.time()
        print("Vehicle parked successfully")

    def vehicle_exit(self):
        vehicle = input("Enter vehicle number: ")

        if vehicle in self.parking:
            entry_time = self.parking.pop(vehicle)
            exit_time = time.time()

            hours = (exit_time - entry_time) / 3600
            fee = round(hours * 20, 2)

            print("Parking Fee:", fee)
        else:
            print("Vehicle not found")

    def show_vehicles(self):
        print("Parked Vehicles:")
        for v in self.parking:
            print(v)
            

pm = ParkingLot()
p = ParkingLot()

while True:
    print("\nParking Lot System")
    print("1.Vehicle Entry")
    print("2.Vehicle Exit")
    print("3.Show Vehicles")
    print("4.Exit")
    

    choice = int(input("Enter choice: "))

    if choice == 1:
        p.vehicle_entry()
    elif choice == 2:
        p.vehicle_exit()
    elif choice == 3:
        p.show_vehicles()
    elif choice == 4:
        break