__author__ = 'baidu'
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack1) == 0:
            print "Error, pop from a empty queue"
            return
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    # @return an integer
    def peek(self):
        if len(self.stack1) == 0:
            print "Error, pop from a empty queue"
            return None
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        result = self.stack2[-1]
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        return result

    # @return an boolean
    def empty(self):
        if len(self.stack1) == 0:
            return True
        else:
            return False
