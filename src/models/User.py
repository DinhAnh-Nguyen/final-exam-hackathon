class User:
    def __init__(self, user_id: int, name: str, vehicle):
        self.user_id = user_id
        self.name = name
        self.vehicle = vehicle
        self.is_handicapped = vehicle.is_handicapped
    
    def set_handicapped(self, is_handicapped: bool):
        self.is_handicapped = is_handicapped

    def get_user_id(self):
        return self.user_id
    def get_name(self):
        return self.name
    def get_vehicle(self):
        return self.vehicle
    def get_is_handicapped(self):
        return self.is_handicapped
    

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, vehicle={self.vehicle.license_plate})"
    
