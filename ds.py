from arr import arr
from dll import dll

class TwoDArr:
    def __init__(self, rows:int = 0, cols:int = 0):
        self.rows = rows
        self.cols = cols
        self.data = arr(rows)
        
        for i in range(rows):
            self.data.insert(i,arr(cols))

    def get_row(self, idx:int) -> arr:
        
        if idx not in range(0,self.rows):
            return False
        
        return self.data.get_by_index(idx)
    
    def get_by_row_col(self, row:int, col:int):
        
        if row not in range(self.rows): return False
        
        if col not in range(self.cols): return False
        
        row:arr = self.get_row(row)
        
        return row.get_by_index(col)
    
    def insert_at_row_col(self, row:int, col:int, data):
        
        if row not in range(self.rows): return False
        
        if col not in range(self.cols): return False
        
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

class hashtable:
    def __init__(self, init_size:int = 8):
        self.table = arr(init_size)
        self.members = 0
        self.g_t = 0.8 #growth threshold

    def hash(self, key:int):
        return key % self.table.size

    def add(self, key:int, data):
        
        print(self.members,'|', self.table.size)

        if self.members / self.table.size >= self.g_t:
            self.add_with_expand(key, data)
        
        else:
            index = self.hash(key)

            if self.table.get_by_index(index) == None:
                self.table.insert(index, dll())
                self.table.get_by_index(index).add_first(key_data(key,data))

            else:
                self.table.get_by_index(index).add_first(key_data(key,data))
            
            self.members += 1
        

    def get_by_key(self, key:int):
        
        dest_list:dll = self.table.get_by_index(self.hash(key))
        
        if dest_list == None: return False

        curr_node = dest_list.head

        while curr_node != None:
            
            if curr_node.data.key == key: 
                return curr_node.data.data
            
            curr_node = curr_node.next

        return False

    def add_with_expand(self, key:int, data):
        
        self.expand()
        self.add(key, data)

    def expand(self):
        
        self.table.expand()
        self.rehash()
        
    def rehash(self):
        old_table = arr(self.table.size)
        #copy old table to rehash into expanded table

        for i in range(self.table.size):
            old_table.insert(i, self.table.get_by_index(i))

        self.table.empty()
        self.members = 0

        for i in range(old_table.size):
            if old_table.get_by_index(i) != None:
                curr_node = old_table.get_by_index(i).head
                
                while curr_node != None:
                    self.add(curr_node.data.key, curr_node.data.data)
                    curr_node = curr_node.next




class key_data:
    def __init__(self, key, data):
        self.key = key
        self.data = data