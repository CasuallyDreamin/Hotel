class dll_node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_first(self, data):
        new_node = dll_node(data)

        if self.head == None:
            self.head = new_node
            self.head.next = new_node

            self.tail = new_node
            self.tail.prev = new_node
            
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_last(self, data):
        new_node = dll_node(data)

        if self.head == None:
            self.head = new_node
            self.head.next = new_node

            self.tail = new_node
            self.tail.prev = new_node
            
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_first(self):
        if self.head == None:
            return
        
        self.head = self.head.next

    def remove_last(self):
        if self.tail == None:
            return
        
        temp = self.tail.prev
        
        if temp != None:
            temp.next = None
        else:
            self.head = None
            self.tail = None


