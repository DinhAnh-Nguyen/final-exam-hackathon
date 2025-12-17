import json
from pathlib import Path
from typing import Any, Dict

from models.ParkingLot import ParkingLot
from models.ParkingSpot import ParkingSpot
from models.Vehicle import Vehicle
from models.User import User


def build_sample_state(json_filename: str = "parkingSpot.json") -> Dict[str, Any]:
    base_dir = Path(__file__).resolve().parents[1]
    data_path = base_dir / json_filename
    if not data_path.exists():
        raise FileNotFoundError(f"JSON file not found at: {data_path}")

    payload = json.loads(data_path.read_text(encoding="utf-8"))

    lot_payload = payload.get("lot", {})
    lot = ParkingLot(
        spotNumber=lot_payload.get("spotNumber", 0),
        id=lot_payload.get("id", "Lot-Unknown"),
        handicappedSpots=lot_payload.get("handicappedSpots", 0),
        availableSpots=lot_payload.get("availableSpots", 0),
    )

    spots = {
        spot_payload["id"]: ParkingSpot(
            spot_payload["id"],
            spot_payload["size"],
            available=spot_payload.get("available", True),
            isHandicapped=spot_payload.get("isHandicapped", False),
        )
        for spot_payload in payload.get("parkingSpots", [])
    }

    vehicles: Dict[str, Vehicle] = {}
    for vehicle_payload in payload.get("vehicles", []):
        plate = vehicle_payload["plate"].upper()
        vehicle = Vehicle(plate, vehicle_payload["size"])
        vehicle.set_handicapped(vehicle_payload.get("handicapped", False))
        vehicles[plate] = vehicle

    users: Dict[int, User] = {}
    for user_payload in payload.get("users", []):
        vehicle = vehicles.get(user_payload["vehiclePlate"].upper())
        if not vehicle:
            continue
        user = User(user_payload["id"], user_payload.get("name", "Unknown"), vehicle)
        user.set_handicapped(user_payload.get("handicapped", False))
        users[user.get_user_id()] = user

    assignments: Dict[str, Dict[str, Any]] = {}
    for item in payload.get("assignments", []):
        plate = item["vehiclePlate"].upper()
        spot = spots.get(item["spotId"])
        user = users.get(item.get("userId"))
        if not (spot and user and vehicles.get(plate)):
            continue
        if spot.is_available():
            spot.park_vehicle()
            lot.park_car()
        assignments[plate] = {"user": user, "spot": spot, "lot": lot}

    return {
        "lot": lot,
        "spots": spots,
        "vehicles": vehicles,
        "users": users,
        "assignments": assignments,
    }
