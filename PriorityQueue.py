import math
from StateNode import StateNode

class PriorityQueue:
    def __init__(self, ele=None):
        self.heap = [ele] if ele != None else [] # min heap of State Nodes

    def enqueue(self, item):
        if not isinstance(item, StateNode):
            return None

        self.heap.append(item)

        child_i = len(self.heap) - 1
        parent_i = PriorityQueue.findParent(child_i)

        while child_i != 0 and item.compareTo(self.heap[parent_i]) <= 0:
            self.swap(child_i, parent_i)
            child_i = parent_i
            parent_i = PriorityQueue.findParent(child_i)
        
        return item
    
    @staticmethod
    def findParent(child_i):
        return math.floor((child_i - 1)/ 2)

    def swap(self, index1, index2):
        temp = self.heap[index2]
        self.heap[index2] = self.heap[index1]
        self.heap[index1] = temp

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        else:
            min = self.heap.pop(0)
            
            # Preserve heap structure

            return min
    
    def min(self):
        return self.heap[0]
    
    def isEmpty(self):
        return len(self.heap) == 0

