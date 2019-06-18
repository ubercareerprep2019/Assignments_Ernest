class disk(object):
    def __init__(self,x):
        self.data = x
    def get_data(self):
        return self.data

class Towers(object):
    def __init__(self,x):
        self.RodA = []
        self.RodB = []
        self.Rodc = []
        while x !=  0 :
            self.RodA.append(disk(x))
            x -= 1
        print("Game has been made!")
    def numberOfDisk(self, rod):
        return len(rod)
    def disksAtRod (self, rod):
        for i in rod:
            print(i.get_data())
    def moveDisk(self,start, end):
        if len(end) == 0:
            movDisk = start.pop()
            end.append(movDisk)
        elif start[len(start)-1].get_data() > end[len(end)-1].get_data():
            print("This is an invlaid move")
        else:
            movDisk = start.pop()
            end.append(movDisk)


# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it
#    on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3. No disk may be placed on top of a smaller disk.


print("Hello welcome to the Towers of Hanoi Game \nReview the rules in the comments")
numDisks =input("How many disks you would like to play with: ")
MyTower = Towers(int(numDisks))
print(MyTower.numberOfDisk(MyTower.RodA))
MyTower.disksAtRod(MyTower.RodA)
MyTower.moveDisk(MyTower.RodA, MyTower.RodB)
MyTower.disksAtRod(MyTower.RodB)
MyTower.moveDisk(MyTower.RodA, MyTower.RodB)
MyTower.disksAtRod(MyTower.RodB)