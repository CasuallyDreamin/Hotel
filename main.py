from hotel import hotel as hot
from user import user
from hotel_time import sys_time, hotel_date, history, record
from room import room
from datetime import datetime

class hotel_sys:
    
    def __init__(self, hotel = None, curr_user = None, years = 1):
        self.hotel:hot = hotel
        self.admin_is_logged = False
        self.curr_user:user = curr_user
        self.time = sys_time()
        self.history = history(years)
    
    def go_next_day(self):
        self.time.go_next_day()

    def init_hotel(self, floor_num):
        try:
            self.hotel = hot(int(floor_num))
        except:
            return 'Invalid floor number'
        
        return True
    
    def sign_up(self, username:str, password:str):
        try:
            username = int(username)
        except:
            return "Invalid username. must be a national ID (numerics only)"
        
        has_special_character = False
        has_capital_letter = False
        has_small_letter = False
        has_number = False

        if len(password) < 5:
            return "Password too short"
        
        for char in password:
            if char in "!@#$%^&*":
                has_special_character = True

            if char in "abcdefghijklmnopqrstuvwxyz":
                has_small_letter = True
        
            if char in "ABCDEFGHIJKLMNOPQESTUVWXYZ":
                has_capital_letter = True

            if char in "1234567890":
                has_number = True
        
        if has_special_character == False:
            return "Must have at least one special character. (!@#$%^&*)"
        
        if has_small_letter == False:
            return "Must have at least one small letter. (a,b,c,d,...)"

        if has_capital_letter == False:
            return "Must have at least one capital letter. (A,B,C,D,...)"
    
        if has_number == False:
            return "Must have at least one number. (1,2,3,4,...)"
        
        self.hotel.users.add(username, user(username, password))
        return True
    
    def login(self, username:str, password:str):
        try:
            username = int(username)
        except:
            return "Invalid Username. must be in national ID format."
        
        new_curr_user:user = self.hotel.users.get_by_key(username)
        
        if new_curr_user == False:
            return "Username not found."
        
        if new_curr_user.password != password:
            return "Wrong password!"

        self.curr_user = new_curr_user

        return True
    
    def res_by_id(self, room_ID:str, start_date:hotel_date, end_date:hotel_date):
        
        to_reserve:room = self.hotel.get_room_by_ID(room_ID)
        
        if to_reserve == 'Invalid room_ID':
            return 'Invalid room_ID.'

        if to_reserve == False:
            return "Room doesn't exist."

        if to_reserve.is_available == False:
            return "Room isn't available."

        try:
            start_date:datetime = datetime(start_date.year,
                                  start_date.month,
                                  start_date.day)
            end_date:datetime = datetime(end_date.year,
                                  end_date.month,
                                  end_date.day)
        except:
            return "Invalid values for start or end date."
        
        if start_date < self.time.time:
            return "Start date cannot be before today."
        
        if start_date > end_date:
            return "End date cannot be before start date."
        
        delta = end_date - start_date

        if delta.days > 7:
            return "Maximum number of days is 7."
        
        ####### VERY IMPORTANT: IMPLEMENT CHECKING IF ROOM IS AVAILABLE IN THE TIME GAP

        reserve_id = start_date.day + end_date.day + int(room_ID)
        
        to_reserve.history.add_record(self.time.year,
                                       self.time.time.date().timetuple().tm_yday,
                                       record(self.time.time.date(),
                                              self.curr_user,
                                              'reserve',
                                              reserve_id))
        
        self.curr_user.history.add_record(self.time.year,
                                       self.time.time.date().timetuple().tm_yday,
                                       record(self.time.time.date(),
                                              self.curr_user,
                                              'reserve',
                                              reserve_id))
        
        self.history.add_record(self.time.year,
                                       self.time.time.date().timetuple().tm_yday,
                                       record(self.time.time.date(),
                                              self.curr_user,
                                              'reserve',
                                              reserve_id))
        
        
        
        





    

    

        



    
