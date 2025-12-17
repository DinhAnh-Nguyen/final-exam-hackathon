class ParkingLot:
    def __init__(self, id, spotNumber, handicappedSpots, availableSpots):
        self.id = id
        self.spotNumber = spotNumber
        self.availableSpots = availableSpots
        self.handicappedSpots = handicappedSpots

    def park_car(self):
        if self.availableSpots > 0:
            self.availableSpots -= 1
            print("Car parked successfully.")
            return True
        else:
            print("No available spots.")
            return False

    def remove_car(self):
        if self.availableSpots < self.spotNumber:
            self.availableSpots += 1
            print("Car removed successfully.")
            return True
        else:
            return False

    def available_spots(self):
        return self.availableSpots

