import time
import copy


### CONSTANTS
m_count = 1000
c_count = 1000
boat_cap = 5

def build_operators():
    return [(x,y) for x in range(0, m_count+1) for y in range(0, c_count+1) if x+y <= boat_cap and x+y > 0]


def state(m1,c1,m2,c2,boat_side):
    return [m1, c1, m2, c2, boat_side, None]

def searchSpace(init):
    start_state = init
    open = list()
    closed = list()
    closed.append(init[:5])
    while not goal(init):
        for iteration in iterate(init):
            if not iteration[:5] in [x[:5] for x in closed]:
                open.append(iteration)
                closed.append(iteration)
                addparent(iteration, init)
        init = open.pop(0)

    parent = init
    order = list()
    while not parent[5] == None:
        order.insert(0,(parent := parent[5])[:5])
        if parent[5] == None:
            break
    for state in order:
        print(str(state).replace(' ', '') + "->", sep='', end='')
    print(str(init[:5]).replace(' ', ''))



def iterate(init):
    return_states = list()
    for operator in build_operators():
        m_change, c_change = operator
        if init[4] == 0:
            new_state = state(init[0]-m_change, init[1]-c_change,init[2]+m_change,init[3]+c_change,1)
            if not badState(new_state):
                return_states.append(new_state)
            else:
                continue
                #print("bad state" + str(new_state))
        else:
            new_state = state(init[0]+m_change, init[1]+c_change, init[2]-m_change,init[3]-c_change, 0)
            if not badState(new_state):
                return_states.append(new_state)
            else:
                continue
                #print("bad state" + str(new_state))
    return return_states


def goal(state):
    if state[0] == 0 and state[1] == 0 and state[2] == m_count and state[3] == c_count and state[4] == 1:
        return True
    else:
        return False
def badState(state):
    if state[0] < state[1] and not state[0] == 0:
        return True
    if state[2] < state[3] and not state[2] == 0:
        return True
    if True in [(x < 0) for x in [state[0], state[1], state[2], state[3]]]:
        return True
    return False
def addparent(child,parent):
    child[5] = parent


try:
    searchSpace(state(m_count,c_count,0,0,0))
except IndexError:
    print("state space not solvable")
