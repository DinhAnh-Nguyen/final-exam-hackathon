from typing import Any, Dict

from models.ParkingLot import ParkingLot
from models.User import User
from models.Vehicle import Vehicle


def build_sample_state() -> Dict[str, Any]:
    lot = ParkingLot(id="Lot-A", maxSpots=10, handicappedSpots=2)

    occupied_spot = lot.spots[0]
    occupied_spot.park_vehicle()

    spots = {spot.id: spot for spot in lot.spots}

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
        "ABC123": {"user": users[1], "spot": occupied_spot, "lot": lot}
    }

    return {
        "lot": lot,
        "spots": spots,
        "vehicles": vehicles,
        "users": users,
        "assignments": assignments,
    }
