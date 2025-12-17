# from models.ParkingLot import ParkingLot
# from models.Vehicle import Vehicle
# from models.User import User
from models.ParkingLot import ParkingLot


if __name__ == "__main__":
    while True:
        print("---------Parking Lot Management System---------")
        print("1. Assign Parking Lot")
        print("2. View Your Registration")
        print("3. Release Parking Lot")
        print("4. Exit")

        try:
            choice = input("Enter your choice (1-4): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting the system. Goodbye!")
            break
        match choice:
            case '1':
                print("View Parking Lots...")
                parkingLot1 = ParkingLot(1, 5, 5)
                parkingLot2 = ParkingLot(2, 5, 5)    
                print("Lot", parkingLot1.id, "\nAvailable Spots:", parkingLot1.available_spots, "\nAvailable Accessibility Spots:", parkingLot1.handicappedSpots, "\n")
                print("Lot", parkingLot2.id, "\nAvailable Spots:", parkingLot2.available_spots, "\nAvailable Accessibility Spots:", parkingLot2.handicappedSpots, "\n")

                try:
                    lotChoice = input("Pick a Parking Lot to park your car (1-2): ").strip()
                    match lotChoice:
                        case '1':
                            print("You have selected Parking Lot 1")
                            parkingLot = parkingLot1
                        case '2':
                            print("You have selected Parking Lot 2")
                            parkingLot = parkingLot2
                        case _:
                            print("Invalid choice. Returning to main menu.")
                            continue

                    userName = input("Enter your name: ").strip()
                    licensePlate = input("Enter your license plate number: ").strip()
                    vehicleType = input("Enter your vehicle size (compact/standard/large): ").strip()

                    parkingLot.park_car()
                    print(f"Parking Lot Assigned for {userName}, License Plate: {licensePlate}, Vehicle Type: {vehicleType}")
                    print(f"Updated Available Spots in Lot {parkingLot.id}: {parkingLot.available_spots}")
                except (KeyboardInterrupt, EOFError):
                    print("\nOperation cancelled. Returning to main menu.")
                    continue
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
