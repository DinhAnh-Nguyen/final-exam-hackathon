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
    
    def park_car(self, user=None, is_handicapped=False):
        if is_handicapped:
            for spot in self.spots:
                if spot.available and spot.is_handicapped_spot():
                    spot.park_vehicle()
                    print(f"Car parked successfully in handicapped spot {spot.id}.")
                    return spot
            print("No available handicapped spots. Trying regular spots...")
        
        for spot in self.spots:
            if spot.available and not spot.is_handicapped_spot():
                spot.park_vehicle()
                print(f"Car parked successfully in spot {spot.id}.")
                return spot
        
        print("No available spots.")
        return None

    def remove_car(self):
        if self.availableSpots < self.spotNumber:
            self.availableSpots += 1
            print("Car removed successfully.")
            return True
        else:
            return False
    

