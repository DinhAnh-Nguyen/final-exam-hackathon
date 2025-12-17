from models.ParkingSpot import ParkingSpot

class ParkingLot:
    def __init__(self, id, maxSpots, handicappedSpots):
        self.id = id
        self.maxSpots = maxSpots
        self.handicappedSpots = handicappedSpots
        self.spots = []
        
        for i in range(1, maxSpots + 1):
            isHandicapped = i <= handicappedSpots
            spot = ParkingSpot(id=i, size="standard", isHandicapped=isHandicapped)
            self.spots.append(spot)
    
    @property
    def available_spots(self):
        return sum(1 for spot in self.spots if spot.available)
    
    def park_car(self):
        for spot in self.spots:
            if spot.available:
                spot.park_vehicle()
                print("Car parked successfully.")
                return True
        print("No available spots.")
        return False

    def remove_car(self):
        if self.availableSpots < self.spotNumber:
            self.availableSpots += 1
            print("Car removed successfully.")
            return True
        else:
            return False
    

