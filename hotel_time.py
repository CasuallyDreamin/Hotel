from datetime import datetime, timedelta


class sys_time:
    def __init__(self):
        self.time:datetime = datetime.now()
        self.year:int = self.time.year
        self.month:int  = self.time.month
        self.day:int = self.time.day

    def go_next_day(self):
        self.time += timedelta(days=1)
        self.year = self.time.year
        self.month = self.time.month
        self.day = self.time.day