#import copy
from Board import manhattan
from Board import copy
from Board import print_board
from PriQue2 import priority_queue

def aStar(board, function):
    open = priority_queue()
    closed = {}
    nodes_expanded = 0
    while not isSolved(board):
        try:
            in_closed = closed[board.key()]
        except KeyError:
            in_closed = False
        for move in board.generateMoves():
            #new_board = copy.deepcopy(board)
            new_board = copy(board)
            new_board.makeMove(move)
            new_board.moves_made += 1
            new_board.moves.append(move)
            cost_to_node = new_board.moves_made + function(new_board)
            if not in_closed:
                open.add(cost_to_node,new_board)
                nodes_expanded += 1
        if not in_closed:
            closed[board.key()] = True
        board = open.get()[0]
    return (board.moves, nodes_expanded)



def isSolved(board):
    return board.b == [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
