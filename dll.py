from arr import arr

class dll_node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.size = 0
        self.head:dll_node = None
        self.tail:dll_node = None
    
    def add_first(self, data):
        new_node = dll_node(data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node

        
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = dll_node(data)

        if self.head == None:
            self.head = new_node
            self.head.next = new_node

            self.tail = new_node
            self.tail.prev = new_node
            
            self.size += 1
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.head == None:
            return
        
        self.head = self.head.next
        self.size -= 1

    def remove_last(self):
        if self.tail == None:
            return
        
        temp = self.tail.prev
        
        if temp != None:
            temp.next = None
        else:
            self.head = None
            self.tail = None
        
        self.size -= 1

    def get_all_arr(self):
        
        curr_node = self.head
        index = 0
        data_arr = arr(self.size)

        while curr_node != None:
            data_arr.insert(index, curr_node.data)
            index += 1
            curr_node = curr_node.next
        
        return data_arr



