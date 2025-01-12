from arr import arr

class TwoDArr:
    def __init__(self, rows:int = 0, cols:int = 0):
        self.rows = rows
        self.cols = cols
        self.data = arr(rows)
        for i in range(rows):
            self.data.add_at_index(i,arr(cols)) 


