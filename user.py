from hotel_time import history

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.history:history = history()
        self.banned = False