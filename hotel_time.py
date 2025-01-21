from datetime import datetime, timedelta
from ds import TwoDArr, hashtable
from arr import arr
class sys_time:
    def __init__(self):
        self.time:datetime = datetime.now()
        self.initial_year:int = self.time.year
        self.year:int = self.time.year
        self.month:int  = self.time.month
        self.day:int = self.time.day

    def go_next_day(self):
        self.time += timedelta(days=1)
        self.year = self.time.year
        self.month = self.time.month
        self.day = self.time.day

class hotel_date:
    def __init__(self, year, month, day):
        self.year:int = year
        self.month:int  = month
        self.day:int = day

class record:
    def __init__(self, date, user, action, ID):
        self.date = date
        self.user = user
        self.action = action
        self.ID = ID


class history:
    def __init__(self, years = 5):
        self.data = TwoDArr(years, 366)
    
    def add_record(self, year, day_of_year, record:record, record_id):
        if self.data.get_by_row_col(year,day_of_year) == None:
            self.data.insert_at_row_col(year, day_of_year, hashtable())

        records_of_day:hashtable = self.data.get_by_row_col(year, day_of_year)
        records_of_day.add(record_id, record)

    def get_record(self, year, day_of_year, record_id)->record:
        if self.data.get_by_row_col(year,day_of_year) == None:
            return False
        
        records_of_day:hashtable = self.data.get_by_row_col(year, day_of_year)
        records_of_day.get_by_key(record_id)
        
        return records_of_day
        

    def get_all_from_date(self, year, day_of_year)->arr:
        if self.data.get_by_row_col(year,day_of_year) == None:
            return False
        
        records_of_day:hashtable = self.data.get_by_row_col(year, day_of_year)

        return records_of_day.get_all_as_arr()
    
        

