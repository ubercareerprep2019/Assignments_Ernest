class Stack(object):
    data = []
    size = 0

    def __init__(self):
        self.data = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def size(self):
         return self.size

    def push(self, x):
        self.size += 1
        self.data.append(x)

    def pop(self):
        if self.size == 0:
            return "Stack is empty"
        else:
            self.size -= 1
            return self.data.pop()

    def top(self):
        return self.data[self.size-1]

# class Queue(object):
#     data = []
#     size = None
#     min = None
#
#     def __init__(self):
#         self.data = []
#         self.size = 0
#         self.min  = 0
#
#     def isEmpty(self):
#         return self.size == 0
#
#     # def size(self):
#     #     return self.size
#
#     def enqueue(self, x):
#         self.size += 1
#         self.data.append(x)
#
#     def dequeue(self):
#         if self.size == 0:
#             return "Stack is empty"
#         else:
#             self.size -= 1
#             return self.data.pop()
#
#     def min(self):
#         return self.min

myStack = Stack()
myStack.push(42)
print ("Printing top of stack after a push: ", myStack.top())
print ( "Printing size (should be 1): ", myStack.size())
popped_value = myStack.pop()
print ("Printing the popped value:", popped_value)




