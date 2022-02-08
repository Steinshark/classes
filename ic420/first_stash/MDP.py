import random

class MDP:
    def __init__(self,states,chance_nodes,start,end,probabilities,rewards):
        self.states = states
        self.chance_nodes = chance_nodes
        self.start = start
        self.end = end
        self.T = probabilities
        self.R = rewards
        self.V = None
        self.Q = None

    def T(s1,a,s2):
        return self.T[str(s1)+str(a)+str(s2)]
    def R(s1,a,s2):
        return self.R[s]
    def run():
        pass
    def V():
        for s in self.states:
            self.V[str(s)] = 0
    def Q():
        for c in self.chance_nodes:
            self.Q[str(c)] = 0
