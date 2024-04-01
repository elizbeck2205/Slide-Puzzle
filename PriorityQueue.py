import math
from StateNode import StateNode
from slide_puzzle import Board

class PriorityQueue:
    def __init__(self, ele=None):
        self.heap = [ele] if ele != None else [] # min heap of State Nodes
        self.length = len(self.heap)

    def enqueue(self, node):
        if not isinstance(node, StateNode):
            return None

        self.heap.append(node)
        self.length += 1

        child_i = self.length - 1
        parent_i = PriorityQueue.findParent(child_i)

        while child_i != 0 and node.compareTo(self.heap[parent_i]) <= 0:
            self.heap[child_i] = self.heap[parent_i]
            self.heap[parent_i] = node
            child_i = parent_i
            parent_i = PriorityQueue.findParent(child_i)
        
        return node
    
    @staticmethod
    def findParent(child_i):
        return math.floor((child_i - 1)/ 2)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            # Delete the first node, save it to min, and set heap[0] to the last node
            min = self.heap[0]
            least_node = self.heap[len(self.heap) - 1]
            self.heap[0] = least_node

            # Change heap length
            self.length -= 1
            self.heap.pop(self.length)


            # Sift the first node down until it's in the right place
            i = 0
            while i*2 < self.length - 1:
                if self.heap[i].compareTo(self.heap[i*2 + 1]) >= 0:
                    self.heap[i] = self.heap[i*2 + 1]
                    self.heap[i*2 + 1] = least_node
                    i = i*2 + 1
                elif self.heap[i].compareTo(self.heap[i*2 + 2]) >= 0:
                    self.heap[i] = self.heap[i*2 + 2]
                    self.heap[i*2 + 2] = least_node
                    i = i*2 + 2
                else:
                    break
            
            print()

            return min
    
    def min(self):
        return self.heap[0]
    
    def isEmpty(self):
        return self.length == 0
