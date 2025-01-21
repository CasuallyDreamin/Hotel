from ds import TwoDArr, queue, hashtable
from hotel_room import room
from dll import dll

class hotel:
    def __init__(self, floors:int = 3):
        self.floors = floors
        self.rooms: TwoDArr = TwoDArr(floors+1, 10)
        self.to_clean: queue = queue()
        self.users: hashtable = hashtable(100)
        self.rooms_added:dll = dll()

    def get_all_rooms(self):
        return self.rooms_added.get_as_list()
    
    def add_room(self, floor:int, num:int, beds:int):
        
        if floor < 0 or floor > self.floors:
            return "invalid floor"

        if num < 0 or num > 9:
            return "invalid room number"

        if beds < 1 or beds > 5:
            return "invalid number of beds"
        
        if self.rooms.get_by_row_col(floor, num) != None:
            return 'room already exists.'
        
        new_room = room(floor, num, beds)
        self.rooms.insert_at_row_col(floor, num, new_room)
        self.rooms_added.add_first(new_room)

        return 'Room added.'
    
    def remove_room(self, room_ID:str):
        
        try:
            floor = int(room_ID[0:-2])
            num = int(room_ID[-1])
        except:
            return "Invalid room_ID"
        
        self.rooms.insert_at_row_col(floor, num, None)

    def get_room_by_ID(self, room_ID:str)->room:

        try:
            floor = int(room_ID[0:-2])
            num = int(room_ID[-1])
        except:
            return "Invalid room_ID"
        target = self.rooms.get_by_row_col(floor, num)

        if target != None:
            if target.beds != int(room_ID[-2]):
                return None
        
        return target 
    