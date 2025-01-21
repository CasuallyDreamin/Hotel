from hotel_time import history
from datetime import datetime
class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.history:history = history()
        self.cancel_count = 0
        unbandate:datetime = None
        self.banned = False

    def get_history_all(self):
        return self.history.get_all_records()