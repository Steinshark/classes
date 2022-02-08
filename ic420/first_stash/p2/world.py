import json
import copy

class World:
    def __init__(self,name):
        self.name = name
        self.input = self.load(name)
        self.shape = self.input["shape"]
        self.gamma = self.input["gamma"]
        self.rewards = self.input["rl"]
        self.terminating_states = self.input["tl"]
        self.blocked = self.input["bl"]
        self.states = self.build_states()
        self.values = self.build_values()
        self.policy = self.build_policy()

    def load(self,name):
        with open(name,'r') as file:
            return json.load(file)

    def build_states(self):
        temp = []
        for row in range(0,self.shape[0]):
            temp.append([])
            for col in range(0,self.shape[1]):
                temp[row].append(State(self.shape,row,col,self.blocked))
                location = [row,col]
                for rew_list in self.rewards:
                    if location == rew_list[0]:
                        temp[row][col].reward = rew_list[1]
                        break
                if location in self.blocked:
                    temp[row][col].blocked = True
        return temp

    def build_values(self):
        temp = []
        for row in range(0,self.shape[0]):
            temp.append([])
            for col in range(0,self.shape[1]):
                temp[row].append(0)
        return temp

    def build_policy(self):
        temp = []
        for row in range(0,self.shape[0]):
            temp.append([])
            for col in range(0,self.shape[1]):
                item = self.states[row][col]
                if item.blocked:
                    temp[row].append("E")
                    continue
                else:
                    temp[row].append("N")
        return temp

    def valueIteration(self,iterations):
        for i in range(0,iterations):
            v_temp = copy.deepcopy(self.values)
            for row in range(0,self.shape[0]):
                for col in range(0,self.shape[1]):
                    if self.states[row][col].reward == 0 and not self.states[row][col].blocked:
                        v_temp[row][col] = self.Vmax(self.states[row][col])
            self.values = v_temp
        for row in range(0,self.shape[0]):
            for col in range(0,self.shape[1]):
                item = self.states[row][col]
                if not item.blocked and item.reward == 0:
                    self.policy[row][col] = self.Pmax(item)
                else:
                    self.policy[row][col] = "."
    def Vmax(self,item):
        Q_vals = []
        #print("on [" + str(item.row) + "," + str(item.col) + "]")
        #print("has neighbors " +str(item.neighbors))
        ## find the Q sum of this node

        for going in ["N","S","E","W"]:
            if going == "N":
                Q_vals.append(((self.computeN(item.row,item.col,.8) + self.computeE(item.row,item.col,.1)+self.computeW(item.row,item.col,.1)), going))
            elif going == "S":
                Q_vals.append(((self.computeS(item.row,item.col,.8) + self.computeE(item.row,item.col,.1)+self.computeW(item.row,item.col,.1)), going))
            elif going == "E":
                Q_vals.append(((self.computeE(item.row,item.col,.8) + self.computeN(item.row,item.col,.1)+self.computeS(item.row,item.col,.1)), going))
            elif going == "W":
                Q_vals.append(((self.computeW(item.row,item.col,.8) + self.computeS(item.row,item.col,.1)+self.computeN(item.row,item.col,.1)), going))
        #print("Q_VALS for [" + str(item.row) + "," + str(item.col) + "]" + " = " + str(Q_vals))
        #print("returns " + str(max([x[0] for x in Q_vals])))
        return  max([x[0] for x in Q_vals])
    def Pmax(self,item):
        Q_vals = []
        #print("on [" + str(item.row) + "," + str(item.col) + "]")
        #print("has neighbors " +str(item.neighbors))
        ## find the Q sum of this node

        for going in ["N","S","E","W"]:
            if going == "N":
                Q_vals.append(((self.computeN(item.row,item.col,.8) + self.computeE(item.row,item.col,.1)+self.computeW(item.row,item.col,.1)), going))
            elif going == "S":
                Q_vals.append(((self.computeS(item.row,item.col,.8) + self.computeE(item.row,item.col,.1)+self.computeW(item.row,item.col,.1)), going))
            elif going == "E":
                Q_vals.append(((self.computeE(item.row,item.col,.8) + self.computeN(item.row,item.col,.1)+self.computeS(item.row,item.col,.1)), going))
            elif going == "W":
                Q_vals.append(((self.computeW(item.row,item.col,.8) + self.computeS(item.row,item.col,.1)+self.computeN(item.row,item.col,.1)), going))
        #print("Q_VALS for [" + str(item.row) + "," + str(item.col) + "]" + " = " + str(Q_vals))
        #print("returns " + str(max([x[0] for x in Q_vals])))
        return  Q_vals[[x[0] for x in Q_vals].index(max([x[0] for x in Q_vals]))][1]

    def computeN(self,row,col,probability):
        if row == 0 or self.states[row-1][col].blocked:
            return self.gamma*self.values[row][col]*probability
        else:
            return probability*(self.states[row-1][col].reward + self.gamma*self.values[row-1][col])
    def computeS(self,row,col,probability):
        if row+1 == self.shape[0] or self.states[row+1][col].blocked:
            return self.gamma*self.values[row][col]*probability
        else:
            return probability*(self.states[row+1][col].reward + self.gamma*self.values[row+1][col])
    def computeE(self,row,col,probability):
        if col+1 == self.shape[1] or self.states[row][col+1].blocked:
            return self.gamma*self.values[row][col]*probability
        else:
            return probability*(self.states[row][col+1].reward + self.gamma*self.values[row][col+1])
    def computeW(self,row,col,probability):
        if col == 0 or self.states[row][col-1].blocked:
            return self.gamma*self.values[row][col]*probability
        else:
            return probability*(self.states[row][col-1].reward + self.gamma*self.values[row][col-1])



class State:
    def __init__(self,shape,row,col,blocked):
        self.N = 0
        self.S = 0
        self.E = 0
        self.W = 0
        self.neighbors = self.neighbors(shape,row,col,blocked)
        self.reward = 0
        self.blocked = False
        self.row = row
        self.col = col

    def __str__(self):
        return str(self.neighbors)
        #return str(self.N) + str(self.E) + str(self.S) + str(self.W) + str(self.reward) + str(self.blocked)
    def neighbors(self,shape,row,col, blocked):
        temp = []
        if not ((row - 1) < 0) and not [row,col] in blocked:
            temp.append("N")
        if not ((row + 1) >= shape[0]) and not [row,col] in blocked:
            temp.append("S")
        if not ((col - 1) < 0) and not [row,col] in blocked:
            temp.append("W")
        if not ((col + 1) >= shape[1]) and not [row,col] in blocked:
            temp.append("E")
        self.bounces = [x for x in ["N","S","E","W"] if not x in temp]
        return temp

    __repr__ = __str__
