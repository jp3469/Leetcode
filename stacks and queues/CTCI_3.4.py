'''
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which you can slide onto any tower.
The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
You have the following constraints:
1. Only one disk can be moved at a time.
2. A disk is slid off the top of one tower onto the next tower.
3. A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks.
'''

class Hanoi:
    def __init__(self, size):
        self.towers = [[], [], []]
        self.size = size
        self.towers[0] = [x for x in range(size, 0, -1)]

    def playHanoi(self):
        self.printTowers()
        self.moveDisk(self.size, 1, 2, 3)
        self.printTowers()

    def moveDisk(self, size, fr, helper, to):
        if size == 1:
            data = self.towers[fr-1].pop()
            self.towers[to-1].append(data)
            print("Disk", data, ":Tower", fr, "->", to)
        else:
            self.moveDisk(size - 1, fr, to, helper)
            self.moveDisk(1, fr, helper, to)
            self.moveDisk(size - 1, helper, fr, to)
    
    def printTowers(self):
        for i in self.towers:
            print(i)

hanoi = Hanoi(7)
hanoi.playHanoi()