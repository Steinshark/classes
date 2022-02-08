import random
class Board():
    # A board is just a 2-d list, plus a location of the blank, for easier move generation.
    def __init__(self):
        self.b = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.lb = [0, 0]
        self.moves_made = 0
        self.moves = []

    #Returns a list of places the blank can be moved to.  Note the use of map and filter.  Good tools for AI
    #programming
    def generateMoves(self):
        delta = [[-1,0],[1,0],[0,-1],[0,1]]
        result = list(map(lambda x: pairAdd(x,self.lb), delta))
        result = list(filter(lambda x: inRange(x), result))
        return result

    #Takes a move location, and actually changes the board.
    def makeMove(self,m):
        # It had better be next to the current location.
        if (manhattan(m,self.lb) > 1):
            raise RuntimeError('Bad move executed on board: ' + str(m) + 'lb: ' + str(self.lb))
        self.b[self.lb[0]][self.lb[1]] = self.b[m[0]][m[1]]
        self.b[m[0]][m[1]] = 'b'
        self.lb = m

    #Mix up the board.
    def scramble(self,n,s=2018):
        random.seed(s)
        for i in range(n):
            moves = self.generateMoves()
            self.makeMove(moves[random.randint(0,len(moves)-1)])

    #are boards equal?
    def __eq__(self,other):
        return self.b == other.b
    def __ne__(self,other):
        return self.b != other.b
    def __lt__(self,other):
        return True
    def key(self):
        return str(self.b)
#---------------------------------
#End of Board class


#apply a list of moves to the board.
def applyMoves(board,moveList):
    for m in moveList:
        board.makeMove(m)


#Some utility functions
def pairAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def inRange(p):
    return p[0] >= 0 and p[0] < 4 and p[1] >=0 and p[1] < 4

#The heuristics go here

# This is not the actual manhattan distance heuristic, but may
# be helpful
def manhattan(a,b):
    #takes two locations on the board and returns the difference
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def print_board(board):
    board = board.b
    for row in board:
        print('\n|',end='')
        for col in row:
            try:
                if col < 10:
                    print(' ',end='')
            except TypeError:
                print(' ', end='')
            print(str(col),end='|')
    print("")

def misplacedTiles(board):
    tb = board.b
    rb = Board().b

    return \
    int(not tb[0][0] == rb[0][0]) + \
    int(not tb[0][1] == rb[0][1]) + \
    int(not tb[0][2] == rb[0][2]) + \
    int(not tb[0][3] == rb[0][3]) + \
    int(not tb[1][0] == rb[1][0]) + \
    int(not tb[1][1] == rb[1][1]) + \
    int(not tb[1][2] == rb[1][2]) + \
    int(not tb[1][3] == rb[1][3]) + \
    int(not tb[2][0] == rb[2][0]) + \
    int(not tb[2][1] == rb[2][1]) + \
    int(not tb[2][2] == rb[2][2]) + \
    int(not tb[2][3] == rb[2][3]) + \
    int(not tb[3][0] == rb[3][0]) + \
    int(not tb[3][1] == rb[3][1]) + \
    int(not tb[3][2] == rb[3][2]) + \
    int(not tb[3][3] == rb[3][3])


def manhattanDistance(board):
    tb = board
    rb = Board().b
    tb.b[tb.lb[0]][tb.lb[1]] = 0
    tb = board.b
    sum = \
    abs(0-int(tb[0][0]/4)) + abs(0-int(tb[0][0]%4)) + \
    abs(0-int(tb[0][1]/4)) + abs(1-int(tb[0][1]%4)) + \
    abs(0-int(tb[0][2]/4)) + abs(2-int(tb[0][2]%4)) + \
    abs(0-int(tb[0][3]/4)) + abs(3-int(tb[0][3]%4)) + \
    abs(1-int(tb[1][0]/4)) + abs(0-int(tb[1][0]%4)) + \
    abs(1-int(tb[1][1]/4)) + abs(1-int(tb[1][1]%4)) + \
    abs(1-int(tb[1][2]/4)) + abs(2-int(tb[1][2]%4)) + \
    abs(1-int(tb[1][3]/4)) + abs(3-int(tb[1][3]%4)) + \
    abs(2-int(tb[2][0]/4)) + abs(0-int(tb[2][0]%4)) + \
    abs(2-int(tb[2][1]/4)) + abs(1-int(tb[2][1]%4)) + \
    abs(2-int(tb[2][2]/4)) + abs(2-int(tb[2][2]%4)) + \
    abs(2-int(tb[2][3]/4)) + abs(3-int(tb[2][3]%4)) + \
    abs(3-int(tb[3][0]/4)) + abs(0-int(tb[3][0]%4)) + \
    abs(3-int(tb[3][1]/4)) + abs(1-int(tb[3][1]%4)) + \
    abs(3-int(tb[3][2]/4)) + abs(2-int(tb[3][2]%4)) + \
    abs(3-int(tb[3][3]/4)) + abs(3-int(tb[3][3]%4))
    tb = board
    tb.b[tb.lb[0]][tb.lb[1]] = 'b'
    return sum


def copy(old_board):
    copy = Board()
    copy.b = [[x for x in item] for item in old_board.b]
    copy.lb = old_board.lb
    copy.moves_made = old_board.moves_made
    copy.moves = [item for item in old_board.moves]
    return copy
