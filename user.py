class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.history = None
        self.banned = False

    def reserve(self, room_ID, time):
        pass