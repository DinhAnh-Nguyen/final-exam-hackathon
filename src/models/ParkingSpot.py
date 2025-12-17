class ParkingSpot:
    def __init__(self, spot_id, size, available=True, isHandicapped=False):
        self.spot_id = spot_id
        self.size = size
        self.available = available
        self.isHandicapped = isHandicapped

    def park_vehicle(self):
        if self.available:
            self.available = False
            return True
        return False

    def remove_vehicle(self):
        if not self.available:
            self.available = True
            return True
        return False