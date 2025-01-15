class room:
    def __init__(self, floor:int, num:int, beds:int):
        self.residency = None
        self.floor = floor
        self.num = num
        self.beds = beds
        self.ID = "{floor}" + "{beds}" + "{num}"
        self.reservation_c = 0
        self.reservation_c_since_service = 0
        self.is_available = True
        self.service = False
        self.history = None
