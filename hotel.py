from ds import TwoDArr, queue, hashtable
from room import room

class hotel:
    def __init__(self, floors:int = 3, years = 1):
        self.floors = floors
        self.rooms: TwoDArr = TwoDArr(floors, 10)
        self.to_clean: queue = queue()
        self.history: TwoDArr = TwoDArr(years, 365)
        self.users: hashtable = hashtable(100)

    def show_2D(self):
        image = ""
        for i in range(self.floors):
            flr = ""
            for j in range(10):
                temp = self.rooms.get_by_row_col(i,j)
                if temp is None: flr += "O"
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
        
        if self.rooms.get_by_row_col(floor, num) != None:
            return 'room already exists.'
        
        self.rooms.insert_at_row_col(floor, num, room(floor, num, beds))
    
    def remove_room(self, room_ID:str):
        
        try:
            floor = int(room_ID[0:-2])
            num = int(room_ID[-1])
        except:
            return "Invalid room_ID"
        
        self.rooms.insert_at_row_col(floor, num, None)

    def get_room_by_ID(self, room_ID:str):

        try:
            floor = int(room_ID[0:-2])
            num = int(room_ID[-1])
        
        except:
            return "Invalid room_ID"
        
        return self.rooms.get_by_row_col(floor, num)
    
m = hotel(4)
m.add_room(1,1,1)
print(m.get_room_by_ID('111').num)
m.show_2D()