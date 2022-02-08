#uses a python tree
class tree:
    def __init__(self,root):
        self.root = root

class node:
    def __init__(self,value):
        self.next = []
        self.value = value
    def add_next(self,node):
        self.next.append(node)
def maxi(state):
    if state.next == None:
        return board_eval(state)
    else:
        list_of_returns = list()
        for child in self.next:
            list_of_returns.append(mini(child))
            return max(list_of_returns)

def mini(state):
    if state.next == None:
        return board_eval(state)
    else:
        list_of_returns = list()
        for child in self.next:
            list_of_returns.append(maxi(child))
            return min(list_of_returns)


init = tree(node(10))


A >=
