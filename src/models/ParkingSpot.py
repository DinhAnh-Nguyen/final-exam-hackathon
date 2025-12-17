class ParkingSpot:
    def __init__(self, id, size, available=True, isHandicapped=False):
        self.id = id
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
    def is_available(self):
        return self.available
    def get_spot_id(self):
        return self.spot_id
    def get_size(self):
        return self.size    
    def is_handicapped_spot(self):
        return self.isHandicapped
    def set_handicapped_spot(self, isHandicapped):
        self.isHandicapped = isHandicapped