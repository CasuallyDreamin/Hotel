class arr:
    def __init__(self, size:int = 1):
        if size <= 0:
            return "Invalid size input"
        
        self.size = size
        self.index_ptr = 0
        self.data:list = self.size * [None]
    
    def add_first(self, data):
        
        temp_index = self.index_ptr

        if temp_index == self.size:
            self.expand()
        
        while temp_index - 1 >= 0:

            self.data[temp_index] = self.data[temp_index - 1]
            temp_index -= 1
        
        self.data[0] = data
        self.index_ptr += 1
        
        return True

    def add_last(self, data):
        
        if self.index_ptr == self.size:
            self.expand()
        
        self.data[self.index_ptr] = data 
        self.index_ptr += 1

        return True

    def add_at_index(self, index, data):
        
        temp_index = self.index_ptr

        if index >= self.size or index < 0:
            return "Out of index"
        
        if index == temp_index:
            self.add_last(data)
            return True
        
        if temp_index == self.size:
            self.expand()

        while temp_index - 1 >= index:

            self.data[temp_index] = self.data[temp_index - 1]
            temp_index -= 1
        
        self.data[index] = data
        self.index_ptr += 1
        
        return True

    def remove_by_index(self, index):
        
        if index >= self.size or index < 0:
            return "Out of index"
        
        while index < self.index_ptr - 1:
            
            self.data[index] = self.data[index + 1]
            index += 1

        self.index_ptr -= 1

        return True
    
    def remove(self, data):
        
        for i in range(self.index_ptr):
            if self.data[i] == data:
                self.remove_by_index(i)
                return True
        
        return "data does not exist"
    
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

def copy_arr(source:list, destination:list):
    
    if len(source) > len(destination):
        return "destination list/array must be bigger than source."
    
    for i in range(len(source)):
        destination[i] = source[i]
    
    return destination


