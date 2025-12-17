from typing import Any, Dict

from models.ParkingLot import ParkingLot
from models.ParkingSpot import ParkingSpot
from models.User import User
from models.Vehicle import Vehicle


def build_sample_state() -> Dict[str, Any]:
    lot = ParkingLot(spotNumber=10, id="Lot-A", handicappedSpots=2, availableSpots=8)

    spots = {
        "P1": ParkingSpot("P1", "compact", available=False),
        "P2": ParkingSpot("P2", "large", available=True, isHandicapped=True),
    }

    vehicles = {
        "ABC123": Vehicle("ABC123", "compact"),
        "XYZ789": Vehicle("XYZ789", "large"),
    }
    vehicles["XYZ789"].set_handicapped(True)

    users = {
        1: User(1, "Mark Bui", vehicles["ABC123"]),
        2: User(2, "Jack Daniel", vehicles["XYZ789"]),
    }
    users[2].set_handicapped(True)

    assignments = {
        "ABC123": {"user": users[1], "spot": spots["P1"], "lot": lot}
    }
    lot.park_car()

    return {
        "lot": lot,
        "spots": spots,
        "vehicles": vehicles,
        "users": users,
        "assignments": assignments,
    }
