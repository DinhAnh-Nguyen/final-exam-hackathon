# from models.ParkingLot import ParkingLot
# from models.ParkingSpot import ParkingSpot
# from models.Vehicle import Vehicle
# from models.User import User

if __name__ == "__main__":
    while True:
        print("---------Parking Lot Management System---------")
        print("1. Assign Parking Lot")
        print("2. View Your Registration")
        print("3. Release Parking Lot")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        match choice:
            case '1':
                print("Assigning Parking Lot...")
            case '2':
                print("Viewing Your Registration...")
            case '3':
                print("Releasing Parking Lot...")
            case '4':
                print("Exiting the system. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")
        print()
