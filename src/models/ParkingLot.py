class ParkingLot:
    def __init__(self, spotNumber, id, handicappedSpots, availableSpots):
        self.id = id
        self.spotNumber = spotNumber
        self.availableSpots = availableSpots
        self.handicappedSpots = handicappedSpots

    def park_car(self):
        if self.availableSpots > 0:
            self.availableSpots -= 1
            return True
        else:
            return False

    def remove_car(self):
        if self.occupied_spots > 0:
            self.occupied_spots -= 1
            return True
        else:
            return False

    def available_spots(self):
        return self.availableSpots

