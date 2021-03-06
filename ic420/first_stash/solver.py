import random
import copy
from queue import PriorityQueue

def aStar(board, function):
    printing = False
    open = PriorityQueue()
    closed = []
    sum = 0
    move_number = 1
    print("started with ")
    print_board(board.b)
    while not isSolved(board):
        if printing:
            print("base board:")
            print_board(board.b)
            print("\nall other boards:")
        for move in board.generateMoves():
            new_board = copy.deepcopy(board)
            new_board.makeMove(move)
            if printing:
                if printing:
                    print_board(new_board.b)
                    print('')
            f_of_n = move_number + 1 + get_manhattan(new_board)
            if not new_board.b in closed:
                sum = sum + 1
                open.put((f_of_n,new_board, move_number+1))
        closed.append(board.b)
        print("length " + str(len(open)))
        board = (chose := open.get())[1]
        move_number = chose[2]
        if printing:
            print("chose ")
            print_board(board.b)
        if printing:
            print("xxxxxxxxxxxxxxxxxxxxxxxxx\n")
        if sum % 100 == 0:
            print("discovered " + str(sum) + " moves")
    print("solved")
    print_board(board.b)


class Board():
    # A board is just a 2-d list, plus a location of the blank, for easier move generation.
    def __init__(self):
        self.b = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.lb = [0, 0]

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

def isSolved(board):
    return board.b == [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

def get_manhattan(puzzle):
    puzzle = puzzle.b
    dimension = len(puzzle)
    sum = 0
    for row in range(0,dimension):
        for col in range(0,dimension):
            actual = puzzle[row][col]
            if 'b' == puzzle[row][col]:
                actual = 0
            sum += (dist := manhattan((row, col),((int(actual/4)),(actual%4))))
            #print(str(actual) + "was distance " + str(dist))
    return sum

def print_board(board):
    for row in board:
        print('\n|',end='')
        for col in row:
            try:
                if col < 10:
                    print(' ',end='')
            except TypeError:
                print(' ', end='')
            print(str(col),end='|')

board = Board()
print(get_manhattan(board))
board.scramble(73)
print_board(board.b)
print(get_manhattan(board))
print(board)
aStar(board, get_manhattan)
