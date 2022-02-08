import random
import string
import pprint
import itertools
import time
import copy

class Target:
    def __init__(self, data, i):
        self.position = data[0:2]
        self.time_to_live = data[2]
        self.available = True
        self.name = string.ascii_uppercase[i]

    def update(self):
        self.time_to_live -= 1
        if self.time_to_live == -1:
            self.available = False

    def __repr__(self):
        return self.name + " " + str(str(self.position) + " @ " + str(self.time_to_live))

class Asset:
    def __init__(self,pos):
        self.position = pos

    def __repr__(self):
        return str(self.position)

class Plan:
    def __init__(self):
        self.targets = list()
        self.assets = list()
        self.obstacles = list()
        self.read_data()
        self.graph = Graph(self.assets,self.targets,self.obstacles,self.dimensions)
        self.graph.build_path()

    def read_data(self):
        filename = str(input("filename: "))
        file = open(filename,'r')

        #READ DIMENSIONS
        self.dimensions = [int(x) for x in file.readline().split(" ")]
        print(self.dimensions)

        #READ OBSTACLES
        file.readline()
        for i in range(int(file.readline())):
            self.obstacles.append([int(x) for x in file.readline().split(" ")])

        #READ ASSETS
        file.readline()
        for i in range(int(file.readline())):
            self.assets.append(Asset([int(x) for x in file.readline().split(" ")]))

        #READ TARGETS
        file.readline()
        for i in range(int(file.readline())):
            self.targets.append(Target([int(x) for x in file.readline().split(" ")], i))

    def build_plan(self):
        pass

    def execute(self):
        pass

class Graph:
    class Node:
        def __init__(self,pos,type):
            self.pos = pos
            self.type = type
        def __repr__(self):
            return str(self.type)

    class Edge:
        def __init__(self,n1,n2,path):
            self.node1 = n1
            self.node2 = n2
            self.len = path[0]
            self.path = path[1]

        def __repr__(self):
            return str(self.node1) + "<->" + str(self.node2)

    def __init__(self,assets,targets,blocked,dimensions):
        self.assets = assets
        self.targets = targets
        self.blocked = blocked
        self.dimensions = dimensions
        print("assets: " + str(len(self.assets)) + " targets: " + str(len(self.targets)))
        print("building nodes ")
        self.build_nodes()
        print("building edges")
        self.build_edges()
        print("init completed for Graph")

    def build_nodes(self):
        t1 = time.time()
        self.nodes = []
        self.real_nodes = []
        self.assetNodes = []
        self.targetNodes = []
        t_counts = 0
        asset_counts = 1
        for y in range(self.dimensions[0]):
            self.nodes.append(list())
            for x in range(self.dimensions[1]):
                temp = None
                if [y,x] in self.blocked:
                    temp = Graph.Node([y,x],'*')
                elif [y,x] in [x.position for x in self.targets]:
                    temp = Graph.Node([y,x], string.ascii_uppercase[t_counts])
                    self.targetNodes.append(temp)
                    t_counts += 1
                elif [y,x] in [x.position for x in self.assets]:
                    temp = Graph.Node([y,x],str(asset_counts))
                    self.assetNodes.append(temp)
                    asset_counts += 1
                else:
                    temp = Graph.Node([y,x],' ')
                self.nodes[y].append(temp)
        self.trim()
        print("took " + str(time.time()-t1))

    def build_edges(self):
        t1 = time.time()
        ## DYKSTRAS EVERY ACTUAL NODE TO EVERY OTHER ACTUAL NODE AND DISCARD THE REST
        self.real_edges = []
        self.real_verts = []
        node_pairings = []
        for item in self.nodes:
            for n1 in item:
                if not n1.type == '*' and not n1.type == ' ':
                    for item2 in self.nodes:
                        for n2 in item2:
                            if not n2.type == '*' and not n2.type == ' ' and not n1 == n2:
                                if {n1,n2} not in node_pairings:
                                    node_pairings.append({n1,n2})
                                    if self.manhattan(n1.pos,n2.pos) < 200:
                                        self.real_edges.append(Graph.Edge(n1,n2,self.dykstras(n1,n2)))

        print("took " + str(time.time()-t1))



    def build_path(self):
        file = open(str(input("out file: ")),'w')
        a = 0
        asset_fives = {}
        asset_moves = {}
        asset_location = {}
        asset_traveled = {}
        ## we'll keep track of the time it takes to reach each target
        target_reached_at = {}
    ## INIT DICTS
        for asset in self.assetNodes:
            asset_fives[asset] = []
            asset_moves[asset] = []
            asset_location[asset] = asset
            asset_traveled[asset] = 0

    ## BUILD TARGETS
        targeted = []
        while not len(targeted) == len(self.targetNodes):
            for asset in self.assetNodes:

                ## CHECK IF THIS NODE IS LEAST
                flag = False
                for asset2 in self.assetNodes:
                    if not asset == asset2:
                        if not (asset_traveled[asset] <= asset_traveled[asset2]):
                            flag = True

                if flag:
                    continue

                ## SOLVE NORMALLY
                print(str(len(targeted)) + " vs total: " + str(len(self.targetNodes)))
                if len(targeted) == len(self.targetNodes):
                    break
                target = self.get_min(asset_location[asset],targeted)
                print(str(asset)+" TARGETS "+str(target))
                targeted.append(target)
                this_edge = self.get_edge(asset_location[asset],target)
                print("edge " + str(this_edge.node1) + "->" + str(this_edge.node2))
                print(this_edge.path)

            ## REVERSE IF THE PATH IS BACKWARDS
                fixed_path = this_edge.path
                if not this_edge.node1 == asset_location[asset]:
                    fixed_path = self.reverse_path(this_edge.path)
            ## ADD THE PATH DIRECIONS TO DICT
                asset_traveled[asset] += len(fixed_path)
                for direction in fixed_path:
                    asset_moves[asset].append(direction)
                asset_location[asset] = target
                asset_traveled[asset] += len(fixed_path)
            ## DEBUG
                print(str(asset)+"->"+str(asset_location[asset]))
                print("")
                ## /DEBUG
    ## WRITE DIRECTIONS TO FILE
        for i in range(0,1000):
            target = True
            for asset in self.assetNodes:
                if i >= len(asset_moves[asset]):
                    asset_location[asset], dir = self.get_safe_edge(asset_location[asset])
                    #print("is safe: " + str(dir))
                    file.write(dir)
                else:
                    file.write(asset_moves[asset][i])
            file.write("\n")
        file.close()
    ## /WRITE DIRECTIONS TO FILE

    def get_edge(self,n1,n2):
        for edge in self.real_edges:
            if {n1,n2} == {edge.node1,edge.node2}:
                return edge

    def get_min(self,node,already):
        min = 100000
        min_node = None
        for edge in self.real_edges:
            n1 = edge.node1
            n2 = edge.node2
            if not node in {n1,n2}:
                continue
            else:
                t_node = {n1,n2} - {node}
                t_node = list(t_node)[0]
                if (t_node in already) or (t_node in self.assetNodes):
                    continue
                else:
                    dist = edge.len
                    if dist < min:
                        min = dist
                        min_node = t_node
        return min_node

    def get_safe_edge(self,node):
        node_list = self.get_neighbors(node.pos[0],node.pos[1])
        num = random.randint(0,3)
        node2,dir = node_list[num]
        while node2 is None:
            num = random.randint(0,3)
            node2, dir = node_list[num]
        return node_list[num]

    def reverse_path(self,path):
        new_path = []
        for direction in reversed(path):
            if direction == "U":
                new_path.append("D")
            elif direction == "D":
                new_path.append("U")
            elif direction == "R":
                new_path.append("L")
            elif direction == "L":
                new_path.append("R")
        return new_path

    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def get_neighbors(self,y,x):
        n = None
        s = None
        e = None
        w = None
        if not y-1 == -1 and not self.nodes[y-1][x].type == '*':
            n = self.nodes[y-1][x]
        if not y+1 >= self.dimensions[0] and not self.nodes[y+1][x].type == '*':
            s = self.nodes[y+1][x]
        if not x+1 >= self.dimensions[1] and not self.nodes[y][x+1].type == '*':
            e = self.nodes[y][x+1]
        if not x-1 == -1 and not self.nodes[y][x-1].type == '*':
            w = self.nodes[y][x-1]
        return ((n,"U"),(s,"D"),(e,"R"),(w,"L"))

    def dykstras(self,node_a,node_b):
        print("dykstras " + str(node_a) + " to " + str(node_b))
        open = priority_queue()
        closed = []
        distances = {node_a:0}
        with_heuristic = {node_a:0}
        parents = {}
        open.add(0,node_a)
        while open.size > 0:
            item, x = open.get()
            closed.append(item)
            if item == node_b:
                path = []
                p = parents[item]
                while not p[0] == node_a:
                    path.insert(0,p[1])
                    p = parents[p[0]]
                path.insert(0,p[1])
                return (len(path), path)
            for neighbor,direction in self.get_neighbors(item.pos[0], item.pos[1]):
                if not neighbor is None and not neighbor in closed:
                    parents[neighbor] = (item,direction)
                    cur_dist = distances[item] + 1
                    try:
                        if distances[neighbor] > cur_dist:
                            distances[neighbor] = cur_dist
                    except KeyError:
                        distances[neighbor] = cur_dist
                    open.add(distances[neighbor] + abs(neighbor.pos[0]-node_b.pos[0])+abs(neighbor.pos[1]-node_b.pos[1]),neighbor)

    def trim(self):
        self.x_left, self.y_top = (0,0)
        self.x_right, self.y_bot = (self.dimensions[1]-1,self.dimensions[0]-1)
        x_pos = [node.pos[1] for node in (self.assetNodes + self.targetNodes)]
        y_pos = [node.pos[0] for node in (self.assetNodes + self.targetNodes)]
        turned = True
        print(str(self.x_left) + " " +   str(self.x_right) + " " +    str(self.y_top) + " " +   str(self.y_bot))
        while turned:
            turned = False
            if not False in (self.x_left < nodes for nodes in x_pos):
                self.x_left += 1
                turned = True
            if not False in (self.x_right > nodes for nodes in x_pos):
                self.x_right -= 1
                turned = True
            if not False in (self.y_top < nodes for nodes in y_pos):
                self.y_top += 1
                turned = True
            if not False in (self.y_bot > nodes for nodes in y_pos):
                self.y_bot -= 1
                turned = True
        print(str(self.x_left) + " " +   str(self.x_right) + " " +    str(self.y_top) + " " +   str(self.y_bot))

        going = True
        if going:
            for y in range(0,self.y_top):
                for x in range(len(self.nodes[y])):
                    self.nodes[y][x] = Graph.Node([y,x],"*")
            for y in range(self.y_bot+1, self.dimensions[0]):
                for x in range(len(self.nodes[y])):
                    self.nodes[y][x] = Graph.Node([y,x],"*")
            for y in range(0,self.dimensions[0]):
                for x_left in range(0,self.x_left):
                    self.nodes[y][x_left] = Graph.Node([y,x_left],"*")
                for x_right in range(self.x_right+1,self.dimensions[1]):
                    self.nodes[y][x_right] = Graph.Node([y,x_right],"*")

    def build_naive_path(self):
        target_health = {}
        print(self.targets)
        for target in self.targets:
            target_health[target] = target.time_to_live
class priority_queue:
    def __init__(self):
        self.value_of = {}
        self.size = 0

    def add(self,value,item):
        self.value_of[item] = (value,item)
        self.size+=1

    def get(self):
        min = 100000
        min_item = None
        for hashed_item in self.value_of.keys():
            current_cost, current_item = self.value_of[hashed_item]
            if current_cost < min:
                min_item = current_item
                min = current_cost
        self.size-=1
        del self.value_of[min_item]
        return min_item, min

    def __repr__(self):
        return str([str(i) + " - " + str(self.value_of[i][0]) for i in self.value_of.keys()])

p = Plan()
