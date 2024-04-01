# Used to represent states of the board
from math import sqrt

class StateNode:
    def __init__(self, state, emptyTileIndex, depth=0):
        self.state = state # the state array
        self.emptyTileIndex = emptyTileIndex
        self.emptyTile = self.getSize()
        self.depth = depth
        self.mt = self.misplacedTiles()
        self.value = depth + self.mt
        self.parentNode = None
    
    def setParent(self, parent):
        self.parentNode = parent
    
    def getParent(self):
        return self.parentNode

    def getSize(self):
        return len(self.state)
    
    def print(self):
        n = int(sqrt(self.getSize()))
        arr = self.state

        for i in range(1, n*n + 1):
            spaces = ' ' * (len(str(n*n)) - len(str(arr[i-1])))
            end_line = '\n' if i%n == 0 else ''
            print(f"{arr[i-1]}{spaces}|", end=end_line)
    
        #print()
    
    def __lt__(self, other):
        return self.value < other.value
    
    def slide(self, i):
        print()
        self.state[self.emptyTileIndex] = self.state[i]
        self.state[i] = self.emptyTile

        # Set blank index
        self.emptyTileIndex = i

        # Reset depth
        self.depth += 1

        # Reset value
        # todo : make more efficient?
        self.mt = self.misplacedTiles()
        self.value = self.depth + self.mt

    def misplacedTiles(self):
        misplacedTiles = 0
        for i in range(self.getSize()):
            if i == self.emptyTileIndex:
                continue
            if self.state[i] != i + 1:
                misplacedTiles += 1
        
        return misplacedTiles