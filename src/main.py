# from models.ParkingLot import ParkingLot
# from models.Vehicle import Vehicle
# from models.User import User
from models.ParkingLot import ParkingLot
from data_loader import build_sample_state


def view_registration(state):
    plate = input("Enter the vehicle license plate: ").strip().upper()
    registration = state["assignments"].get(plate)
    if not registration:
        print(f"No registration found for license plate {plate}.")
        return

    user = registration["user"]
    spot = registration["spot"]
    lot = registration["lot"]
    vehicle = user.get_vehicle()

    print("--- Registration Details ---")
    print(f"User ID: {user.get_user_id()}")
    print(f"Name: {user.get_name()}")
    print(f"Vehicle: {vehicle.get_license_plate()} ({vehicle.get_vehicle_type()})")
    print(f"Handicapped: {'Yes' if user.get_is_handicapped() else 'No'}")
    print(f"Assigned Lot: {lot.id} - Spot: {spot.id} ({spot.size})")
    print(f"Spot Type: {'Handicapped' if spot.is_handicapped_spot() else 'Standard'}")


def release_parking_spot(state):
    plate = input("Enter the vehicle license plate to release: ").strip().upper()
    registration = state["assignments"].get(plate)
    if not registration:
        print(f"No active assignment found for license plate {plate}.")
        return

    spot = registration["spot"]
    lot = state["lot"]
    if spot.remove_vehicle():
        print(f"Released spot {spot.id} for vehicle {plate}.")
        print(f"Updated available spots in lot {lot.id}: {lot.available_spots}")
    else:
        print(f"Spot {spot.id} was already available.")

    del state["assignments"][plate]


def main():
    state = build_sample_state()
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
                view_registration(state)
            case '3':
                release_parking_spot(state)
            case '4':
                print("Exiting the system. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")
        print()


if __name__ == "__main__":
    main()
