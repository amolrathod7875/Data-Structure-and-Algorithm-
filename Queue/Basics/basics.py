class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Queue is Empty")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError('Queue is Empty')
    
    def is_empty(self):
        return len(self.queue) == 0 

    def size(self):
        return len(self.queue)
