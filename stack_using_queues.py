import Queue
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.a = Queue.Queue(100)
        self.b = Queue.Queue(100)

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.a.qsize() > 100:
            return
        self.a.put(x)

    # @return nothing
    def pop(self):
        while self.a.qsize() > 1:
            self.b.put(self.a.get())
        self.a.get()
        while self.b.qsize() > 0:
            self.a.put(self.b.get())

    # @return an integer
    def top(self):
        while self.a.qsize() > 1:
            self.b.put(self.a.get())
        result = self.a.get()
        while self.b.qsize() > 0:
            self.a.put(self.b.get()) 
        self.a.put(result)
        return result
    # @return an boolean
    def empty(self):
        if self.a.qsize() == 0:
            return True
        else:
            return False
        