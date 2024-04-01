#from PriorityQueue import PriorityQueue
from StateNode import StateNode
from math import sqrt
from slide_puzzle import Board
from copy import deepcopy
import heapq

class AStar:
    def __init__(self, initialNode, goalNode):
        self.queue = [initialNode]
        self.goalnode = goalNode
        self.hash_set = set()
        self.hash_set.add(initialNode)
        print()

    def execute(self):
        while not len(self.queue) == 0:
            currentNode = heapq.heappop(self.queue)

            # Add currentNode to hash_set
            self.hash_set.add(currentNode)

            currentNode.print()
            if currentNode.getParent() != None:
                print('Parent: ')
                currentNode.getParent().print()
            print()

            if currentNode == self.goalnode:
                return currentNode

            # Add currentNode's children to the queue
            
            neighbors = self.neighbors(currentNode)

            for move_index in neighbors:
                newNode = deepcopy(currentNode)
                newNode.slide(move_index)
                newNode.setParent(currentNode)
                if newNode not in self.hash_set:
                    heapq.heappush(self.queue, newNode)
                    self.hash_set.add(newNode)
            
            print()
        
        return None
    
    def neighbors(self, node):
        n = int(sqrt(node.getSize()))
        neighbors = []

        # Is right slide possible
        if node.emptyTileIndex % n != 0:
            neighbors.append(node.emptyTileIndex - 1)
        
        # Is left slide possible
        if node.emptyTileIndex % n < n - 1:
            neighbors.append(node.emptyTileIndex + 1)
        
        # Is up slide possible
        if node.emptyTileIndex < node.getSize() - n:
            neighbors.append(node.emptyTileIndex + n)
        
        # Is down slide possible
        if node.emptyTileIndex > n - 1:
            neighbors.append(node.emptyTileIndex - n)
        
        return neighbors
    
    
if __name__ == '__main__':
    board = Board(4) # 4x4 board
    initialnode = StateNode(board.arr, board.blank_index)
    goalnode = StateNode([x for x in range(1, 17)], 15)
    astar = AStar(initialnode, goalnode)
    astar.execute()

    print()