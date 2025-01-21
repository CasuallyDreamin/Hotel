from hotel import hotel as hot
from user import user
from hotel_time import sys_time, hotel_date, history, record
from hotel_room import room
from datetime import datetime, timedelta
from random import randint

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

        if to_reserve == None:
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

        duration = delta.days

        reserve_id = randint(0,999999)

        if to_reserve.check_availablity(start_date, end_date) == False:
            return "Room is not available for the requested time frame."
        
        new_record = record(start_date,
                            end_date,
                            self.curr_user,
                            'reserve',
                            reserve_id,
                            to_reserve,
                            self.time.time.date())                                       
                        
        to_reserve.handle_record(new_record, duration)
        
        self.curr_user.history.add_record(self.time.year,
                                       self.time.time.date().timetuple().tm_yday,
                                       new_record,
                                       new_record.ID)
        
        self.history.add_record(self.time.year,
                                       self.time.time.date().timetuple().tm_yday,
                                       new_record,
                                       new_record.ID)
        
        if to_reserve.service == True:
            self.hotel.to_clean.enqueue(to_reserve)

        return True
        
        
    def cancel_by_id(self, record_ID:int, date:datetime, reason):

        record_to_cancel:record = self.history.get_record(date.year,
                                                        date.date().timetuple().tm_yday,
                                                        record_ID)
        
        if record_to_cancel == False:
            return 'record not found (Check record ID)'
        
        if record_to_cancel.action == "cancel":
            return 'cannot cancel a cancelation!'
        
        dura = (record_to_cancel.end_date - record_to_cancel.start_date).days
        
        record_to_cancel.room.handle_record(record_to_cancel, dura)

        new_cancel_record = record(record_to_cancel.start_date,
                                   record_to_cancel.end_date,
                                   record_to_cancel.user,
                                   'cancel',
                                   record_to_cancel.ID + 1,
                                   record_to_cancel.room,
                                   self.time.time.date(),
                                   info = reason
                                )
        
        self.history.add_record(self.time.year,
                                self.time.time.date().timetuple().tm_yday,
                                new_cancel_record,
                                new_cancel_record.ID
                                )
        
        self.curr_user.history.add_record(self.time.year,
                                self.time.time.date().timetuple().tm_yday,
                                new_cancel_record,
                                new_cancel_record.ID
                                )
        
        self.curr_user.cancel_count += 1
        
        if self.curr_user.cancel_count == 3:
            self.curr_user.cancel_count = 0
            self.curr_user.banned = True
            dt = timedelta(2)
            curr_time = self.time.time
            self.curr_user.unban_date = curr_time + dt 
        return True
    
        
        
        





    

    

        



    
