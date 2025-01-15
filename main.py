from hotel import hotel as hot
from user import user

class hotel_sys:
    
    def __init__(self, hotel = None, curr_user = None):
        self.hotel:hot = hotel
        self.curr_user:user = None

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

        return "Welcome!"
    

    

        



    