from arr import arr
from dll import dll

class TwoDArr:
    def __init__(self, rows:int = 0, cols:int = 0):
        self.rows = rows
        self.cols = cols
        self.data = arr(rows)
        for i in range(rows):
            self.data.insert(i,arr(cols))

    def get_row(self,idx:int):
        if idx not in range(0,self.rows):
            return False
        
        return self.data.get_by_index(idx)
    
    def get_by_row_col(self, row:int, col:int):
        
        if row not in range(self.rows):
            return False
        
        if col not in range(self.cols):
            return False
        
        row:arr = self.get_row(row)
        return row.get_by_index(col)
    
    def insert_at_row_col(self, row:int, col:int, data):
        
        if row not in range(self.rows):
            return False
        
        if col not in range(self.cols):
            return False
        
        row:arr = self.get_row(row)
        row.insert(col, data)
    
class stack:
    def __init__(self):
        self.top = None
        self.data = dll()

    def push(self, data):
        self.top = data
        self.data.add_first(data)

    def pop(self):
        temp = self.top
        self.data.remove_first()
        self.top = self.data.head
        return temp
    
    def get_top(self):
        return self.top
    
class queue:
    def __init__(self):
        self.first = None
        self.data = dll()

    def enqueue(self, data):
        if self.first == None:
            self.first = data
        
        self.data.add_last(data)

    def dequeue(self):
        temp = self.first
        self.data.remove_first()
        self.first = self.data.head
        return temp

