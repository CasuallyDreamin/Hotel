from ds import TwoDArr
from room import room
from arr import arr

class hotel:
    def __init__(self, floors:int = 3):
        self.floors = floors
        self.rooms = TwoDArr(floors, 10)

    def show_2D(self):
        image = ""
        for floor in self.rooms.data.data:
            flr = ""
            for room in floor.data:
                if room is None: flr += "O"
                else: flr += "R"
            image = flr + '\n' + image 

        print(image)
    
    def add_room(self, floor:int, num:int, beds:int):
        
        if floor < 0 or floor > self.floors:
            return "invalid floor"

        if num < 0 or num > 9:
            return "invalid room number"

        if beds < 1 or beds > 5:
            return "invalid number of beds"

        dest_floor:arr = self.rooms.data.data[floor-1]
        dest_floor.data[num] = room(floor, num, beds)
    
    def remove_room(self, room_ID:str):
        
        try:
            col = int(room_ID[-2])
            row = int(room_ID[0:-2])
        except:
            return "Invalid room_ID"
        
        dest_floor:arr = self.rooms.data.data[row-1]
        dest_floor.data[col] = None

    def get_room_by_ID(self, room_ID):

        try:
            col = int(room_ID[-2])
            row = int(room_ID[0:-2])
        except:
            return "Invalid room_ID"
        
        dest_floor:arr = self.rooms.data.data[row-1]
        return dest_floor.data[col]