from collections import deque
from Board import Board
class priority_queue:
    def __init__(self):
        self.priorityQueue = deque()
    def add(self,new_value,new_item):
        #turns out it ran much faster if we never check to update values
        self.priorityQueue.append((new_item,new_value))

    def get(self):
        min_val = 999999
        min_item = self.priorityQueue[0]
        for item in self.priorityQueue:
            value = item[1]
            if value < min_val:
                min_item = item
                min_val = value
            elif value == min_val:
                #if we remove the larger moves made, it means the board heuristic is lower (better)
                if item[0].moves_made > min_item[0].moves_made:
                    min_item = item
                    min_val = value
        return_val = min_item
        self.priorityQueue.remove(min_item)
        return return_val
