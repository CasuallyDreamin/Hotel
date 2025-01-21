from datetime import datetime, timedelta
from ds import TwoDArr, hashtable, dll
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
    def __init__(self,
                start_date:datetime,
                end_date:datetime,
                user,
                action,
                ID,
                room,
                record_date,
                info = ''):
        
        self.start_date:datetime = start_date
        self.end_date:datetime = end_date
        self.user = user
        self.action:str = action
        self.ID:int = ID
        self.room = room
        self.record_date = record_date
        self.info = ''


class history:
    def __init__(self, years = 5, initial_year = 2025):
        self.data = TwoDArr(years, 366)
        self.initial_year = initial_year
    
    def add_record(self, year:int, day_of_year:int, record:record, record_id:int):

        if self.data.get_by_row_col(year - self.initial_year ,day_of_year) == None:
            self.data.insert_at_row_col(year - self.initial_year, day_of_year, hashtable())
            records_of_day:hashtable = self.data.get_by_row_col(year - self.initial_year, day_of_year)
            records_of_day.add(record_id, record)
        else:
            records_of_day:hashtable = self.data.get_by_row_col(year - self.initial_year, day_of_year)
            records_of_day.add(record_id, record)

    def get_record(self, year:int, day_of_year:int, record_id:int) -> record:
        if self.data.get_by_row_col(year,day_of_year) == None:
            return False
        
        records_of_day:hashtable = self.data.get_by_row_col(year - self.initial_year, day_of_year)
        dest_record:record = records_of_day.get_by_key(record_id)
        
        return dest_record
        

    def get_all_from_date(self, year:int, day_of_year:int) -> arr:
        if self.data.get_by_row_col(year,day_of_year) == None:
            return False
        
        records_of_day:hashtable = self.data.get_by_row_col(year - self.initial_year, day_of_year)

        return records_of_day.get_all_data_as_arr()
    
    def get_all_records(self):
        all_data_arr_of_hts:arr = self.data.get_all_data()
        temp = dll()

        for i in range(all_data_arr_of_hts.size):
            curr_ht = all_data_arr_of_hts.get_by_index(i)
            curr_ht_arr = curr_ht.get_all_data_as_arr()

            for j in range(curr_ht.members):
                temp.add_first(curr_ht_arr.get_by_index(j))


        return temp.get_as_list()
        

