class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self): #return the top element of the stack without removing it
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    # Test code
    s=Stack()
    for i in range(5):
        s.push(i)
        print(s)
    print(s.isEmpty())
    for i in range(5):
        print(s.pop(),s)
    print(s.isEmpty())