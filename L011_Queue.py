class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def __str__(self):
        return str(self.queue)
    

if __name__ == "__main__":
    # Test code
    q=Queue()

    for i in range(5):
        q.enqueue(i)
        print(q)
    print(q.is_empty())
    for i in range(5):
        print(q.dequeue(),q)
    print(q.is_empty())