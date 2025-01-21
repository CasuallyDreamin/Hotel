class arr:
    def __init__(self, size:int = 1):
        
        if size < 0:
            return "Invalid size input"
        
        self.size = size
        self.data:list = self.size * [None]
    
    
    def insert(self, index:int, data):

        if index >= self.size or index < 0:
            return "Out of index"
        
        
        self.data[index] = data
        
        return True

    def remove_by_index(self, index:int):
        
        if index >= self.size or index < 0:
            return False

        self.data[index] = None

        return True
    
    def remove(self, data):
        
        for i in range(self.index_ptr):
            if self.data[i] == data:
                self.remove_by_index(i)
                return True
        
        return False
    
    def show_all(self):
        
        data = '|'
        
        for i in range(self.size):
            data += str(self.data[i]) + '|'
        
        print(data)

    def expand(self):

        new_size = self.size * 2
        new_data_arr = new_size * [None]
        
        self.data = copy_arr(self.data, new_data_arr)

        self.size = new_size

        return True
    
    def get_by_index(self, idx):
        if idx < 0 or idx > self.size:
            return 'Out of index'
        
        return self.data[idx]
    
    def empty(self):
        self.data = self.size * [None]

def copy_arr(source:list, destination:list):
    
    if len(source) > len(destination):
        return "destination list/array must be bigger than source."
    
    for i in range(len(source)):
        destination[i] = source[i]
    
    return destination


