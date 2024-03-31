from PriorityQueue import PriorityQueue
from StateNode import StateNode
from math import sqrt
from slide_puzzle import Board
from copy import deepcopy

class AStar:
    def __init__(self, initialNode, goalNode):
        self.queue = PriorityQueue(initialNode)
        self.goalnode = goalNode
        self.hash_set = set()
        self.hash_set.add(initialNode)
        print()

    def execute(self):
        while not self.queue.isEmpty():
            currentNode = self.queue.dequeue()

            # Add currentNode to hash_set
            self.hash_set.add(currentNode)

            currentNode.print()
            if currentNode.getParent() != None:
                print('Parent: ')
                currentNode.getParent().print()
            print()

            if currentNode.compareTo(self.goalnode) == 0:
                return currentNode

            # Add currentNode's children to the queue
            
            n = int(sqrt(currentNode.getSize()))

            # Is right slide possible?
            if currentNode.emptyTileIndex % n != 0:
                newNode = deepcopy(currentNode)
                newNode.slide(newNode.emptyTileIndex - 1)
                newNode.setParent(currentNode)
                if newNode not in self.hash_set:
                    self.queue.enqueue(newNode)
                print()
            
            # Is left slide possible?
            if currentNode.emptyTileIndex % n < n - 1:
                newNode = deepcopy(currentNode)
                newNode.slide(newNode.emptyTileIndex + 1)
                newNode.setParent(currentNode)
                if newNode not in self.hash_set:
                    self.queue.enqueue(newNode)
                print()
            
            # Is up slide possible?
            if currentNode.emptyTileIndex < currentNode.getSize() - n:
                newNode = deepcopy(currentNode)
                newNode.slide(newNode.emptyTileIndex + n)
                newNode.setParent(currentNode)
                if newNode not in self.hash_set:
                    self.queue.enqueue(newNode)
                print()

            # Is down slide possible?
            if currentNode.emptyTileIndex > n - 1:
                newNode = deepcopy(currentNode)
                newNode.slide(newNode.emptyTileIndex - n)
                newNode.setParent(currentNode)
                if newNode not in self.hash_set:
                    self.queue.enqueue(newNode)
                print()
            
            print()
        
        return None
    
    
if __name__ == '__main__':
    board = Board(4) # 4x4 board
    initialnode = StateNode(board.arr, board.blank_index)
    goalnode = StateNode([x for x in range(1, 17)], 15)
    astar = AStar(initialnode, goalnode)
    astar.execute()

    print()