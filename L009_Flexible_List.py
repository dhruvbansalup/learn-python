class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        return

    def isempty(self):
        if self.data == None:
            return True
        else:
            return False
    
    #recursive function to append data to the end of the list
    def append(self,data):
        if self.isempty():
            self.data = data
        elif self.next == None:
            self.next = Node(data)
        else:
            self.next.append(data)
        return
    #iterative function to append data to the end of the list
    def appendi(self,data):
        if self.isempty():
            self.data = data
        else:
            current = self
            while current.next != None:
                current = current.next

            current.next = Node(data)
        return
    
    def insert(self,data):
        if self.isempty():
            self.data = data
        
        else:
            new_node = Node(data)

            #Exchange data in self and newnode
            self.value,new_node.value = new_node.value,self.value
            
            #switch links
            self.next,new_node.next = new_node,self.next
        return
    
    #recursive function to delete data from the list
    def delete(self,data):
        if self.isempty():
            return
    
        if self.data == data:
            self.data = None
            if self.next != None:
                self.data = self.next.data
                self.next = self.next.next
            return
        else:
            if self.next!=None:
                self.next.delete(data)
                if self.next.data == None:
                    self.next = None
        return