class Stack(object):
    data = []
    length = 0

    def __init__(self):
        self.data = []
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def size(self):
         return self.length

    def push(self, x):
        self.length += 1
        self.data.append(x)

    def pop(self):
        if self.length == 0:
            return "Stack is empty"
        else:
            self.length -= 1
            return self.data.pop()

    def top(self):
        return self.data[self.length - 1]

class Queue(object):
    data = []
    length = 0
    minimum = 0

    def __init__(self):
        self.data = []
        self.length = 0
        self.minimum   = 0

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def enqueue(self, x):
        self.length += 1
        self.data.append(x)

    def dequeue(self):
        if self.length == 0:
            return "Queue is empty"
        else:
            self.length -= 1
            return self.data.pop(0)

    def min(self):
        if self.length == 0:
            return "Queue is empty"
        else:
            newList = sorted(self.data)
            return newList[0]


myStack = Stack()
myStack.push(42)
print ("Printing top of stack after a push: ", myStack.top())
print ( "Printing size (should be 1): ", myStack.size())
popped_value = myStack.pop()
print ("Printing the popped value:", popped_value)


myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(4)
myQueue.enqueue(3)
myQueue.enqueue(13)
myQueue.enqueue(2)
myQueue.enqueue(-19)
print (myQueue.dequeue())
print (myQueue.dequeue())
print (myQueue.min())


