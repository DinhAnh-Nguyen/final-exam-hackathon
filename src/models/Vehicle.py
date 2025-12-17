class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: str):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.is_handicapped = False 

    def set_handicapped(self, is_handicapped: bool):
        self.is_handicapped = is_handicapped    
    def get_license_plate(self):
        return self.license_plate
    def get_vehicle_type(self):
        return self.vehicle_type
    def get_is_handicapped(self):
        return self.is_handicapped
    def __str__(self):
        return f"Vehicle(license_plate={self.license_plate}, vehicle_type={self.vehicle_type}, is_handicapped={self.is_handicapped})"

    
    