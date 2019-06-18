class Node(object):
    def __init__(self,x):
        self.data = x
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class Linked_list(object):
    def __init__(self):
        self.tail = Node(None)
        self.length = None

    def size (self):
        return self.length

    def pushBack(self, x):
        new_Node = Node(x)
        new_Node.next = self.tail
        self.tail = new_Node
        if self.length == None:
            self.length = 1
        else:
            self.length +=1

    def popBack(self):
        if self.length == 0 or None:
            return "No elements to remove "
        else:
            self.tail = self.tail.next
            self.length -=1

    def insert(self,index, newNode):
        newNode = Node(newNode)
        if index > self.length or index < 0:
            return "Not a valid index"
        else:
            counter = (self.length - index) -1
            temp = self.tail
            while counter != 0:
                temp = temp.next
                counter -= 1
            newNode.next = temp.next
            temp.next = newNode
            self.length += 1

    def erase(self,index):
        if index > self.length or index < 0:
            return "Not a valid index"
        else:
            counter = (self.length - index) -1
            temp = self.tail
            while counter != 1:
                temp = temp.next
                counter -= 1
            temp2 = temp.next
            temp.next =temp2.next
            self.length -=1

    def elementAt(self,index):
        if index > self.length or index < 0:
            return "Not a valid index"
        else:
            counter = (self.length - index) - 1
            temp = self.tail
            while counter != 0:
                temp = temp.next
                counter -= 1
            return temp

    def hasCycle(self):
        i = 0
        temp = self.tail
        while i != self.length:
            if temp.get_data() == None:
                return False
            i += 1
        return True

    def isPalindrome(self):
        i = 0
        temp = self.tail
        elements = []
        while i != self.length:
            elements.append(temp.get_data())
            temp = temp.next
            i += 1
        reversedElements = elements[::-1]
        if elements == reversedElements:
            return True
        else:
            return False




myList = Linked_list()
myList.pushBack(21)
myList.pushBack(16)
myList.pushBack(19)
myList.pushBack(50)
myList.pushBack(60)
print(myList.size())
print((myList.elementAt(myList.length-1)).get_data())
myList.popBack()
print((myList.elementAt(myList.length-1)).get_data())
print(myList.size())
print((myList.elementAt(1)).get_data())
myList.erase(1)
print((myList.elementAt(1)).get_data())
myList.insert(1,100)
print((myList.elementAt(1)).get_data())
print((myList.elementAt(100)))
print(myList.erase(100))
myList2 = Linked_list()
myList2.pushBack(1)
myList2.pushBack(2)
myList2.pushBack(3)
myList2.pushBack(2)
myList2.pushBack(1)
print(myList2.isPalindrome())


