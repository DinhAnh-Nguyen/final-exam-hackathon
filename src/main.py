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
    print(
        f"Assigned Lot: {lot.get_id()} - Spot: {spot.get_spot_id()} ({spot.get_size()})"
    )
    print(f"Spot Type: {'Handicapped' if spot.is_handicapped_spot() else 'Standard'}")


def main():
    state = build_sample_state("parkingSpot.json")
    while True:
        print("---------Parking Lot Management System---------")
        print("1. Assign Parking Lot")
        print("2. View Your Registration")
        print("3. Release Parking Lot")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        match choice:
            case "1":
                print("Assigning Parking Lot...")
            case "2":
                view_registration(state)
            case "3":
                print("Releasing Parking Lot...")
            case "4":
                print("Exiting the system. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")
        print()


if __name__ == "__main__":
    main()
