class Linked_List_Node(object):
    value = 0
    next = None

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
