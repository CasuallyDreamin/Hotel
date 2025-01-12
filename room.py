class room:
    def __init__(self, floor:int, num:int, beds:int):
        self.floor = floor
        self.num = num
        self.beds = beds
        self.ID = "{floor}" + "{num}" + "{beds}"
        self.res_c = 0
        self.res_c_since_service = 0
        self.is_available = True
        self.service = False

