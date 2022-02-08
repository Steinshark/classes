import time
import matplotlib.pyplot as plt
import itertools
from astar import *
from idastar import *
from Board import *
import random

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self,depth,int1,int2):
        self.root = None
        self.depth = depth
        self.build_random_tree(0,int1,int2)

    def add_nodes(self,current,depth,int1,int2):
        if self.depth <= depth:
            return
        else:
            current.left = Node(random.randint(int1,int2))
            current.right = Node(random.randint(int1,int2))
            self.add_nodes(current.left,depth+1,int1,int2)
            self.add_nodes(current.right,depth+1,int1,int2)

    def build_random_tree(self,depth,int1,int2):
        self.root = Node(random.randint(int1,int2))
        current = self.root
        self.add_nodes(current,depth,int1,int2)

    def full_trav(self):
        self.nodes = 0
        self.traverse(self.root)

    def traverse(self,node):
        self.nodes += 1
        if node.left == None and node.right == None:
            print(node.value)
        else:
            self.traverse(node.left)
            self.traverse(node.right)
    def full_max(self):
        self.node_path = []
        self.find_max(self.root)
        return self.node_path

    def find_max(self,node):
        if node.left == None and node.right == None:
            return node.value
        else:
            left = node.value + self.find_max(node.left)
            right = node.value + self.find_max(node.right)
            if left > right:
                return left
            else:
                return right


class QBert:
    def __init__(self):
        self.count = 0
        self.tree = Tree(10,1,10)
        self.dictionary = {}


a = QBert()
a.tree.full_trav()
print(a.tree.full_max())
