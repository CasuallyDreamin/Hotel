from user import user
from hotel_time import history
from datetime import datetime, timedelta
from arr import arr
from ds import TwoDArr

class room:
    def __init__(self, floor:int, num:int, beds:int):
        self.residency:user = None
        self.floor = floor
        self.num = num
        self.beds = beds
        self.ID = f"{self.floor}" + f"{self.beds}" + f"{self.num}"
        self.reservation_c = 0
        self.reservation_c_since_service = 0
        self.is_available = True
        self.service = False
        self.service_date = None
        self.history = history()
        self.history_bit_array = TwoDArr(5, 366)

    def check_availablity(self, start_date:datetime, end_date:datetime, initial_year:int = 2025):

        duration = (end_date - start_date).days + 1
        day_index = start_date.date().timetuple().tm_yday
        

        for i in range(duration):
            if self.history_bit_array.get_by_row_col(start_date.year - initial_year, day_index + i) != None:
                return False
            
        return True
    
    def handle_record(self, record, duration = 0):
        if record.action == 'reserve':
            self.history.add_record(record.start_date.year,
                                    record.start_date.date().timetuple().tm_yday,
                                    record,
                                    record.ID)
            
            for i in range(record.start_date.year - self.history.initial_year,
                            record.end_date.year - self.history.initial_year + 1):
                
                for j in range(record.start_date.date().timetuple().tm_yday,
                               record.end_date.date().timetuple().tm_yday + 1):
                    self.history_bit_array.insert_at_row_col(i, j, True)
            
            self.reservation_c += duration
            self.reservation_c_since_service += duration

            if self.reservation_c_since_service >= 10:
                self.reservation_c_since_service = 0
                self.is_available = False
                self.service = True
                dtime = timedelta(1)
                self.service_date = record.end_date + dtime

        if record.action == 'cancel':
            self.history.add_record(record.start_date.year,
                                    record.start_date.date().timetuple().tm_yday,
                                    record,
                                    record.ID)
            
            for i in range(record.start_date.year - self.history.initial_year,
                            record.end_date.year - self.history.initial_year + 1):
                
                for j in range(record.start_date.date().timetuple().tm_yday,
                               record.end_date.date().timetuple().tm_yday + 1):
                    
                    self.history_bit_array.insert_at_row_col(i, j, None)

            self.reservation_c -= duration
            self.reservation_c_since_service -= duration

            if self.reservation_c_since_service < 10:
                self.is_available = True
                self.service = False
                self.service_date = None
            
