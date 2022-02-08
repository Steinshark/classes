from Board import copy
from collections import deque

def idaStar(board,function):
    limit = board.moves_made + function(board)
    r = 0
    nodes_expanded = 0
    while isNumber(r):
        r, nodes_expanded = FlimitDFS(board,limit,function, nodes_expanded)
        if isNumber(r):
            limit = r
    return r, nodes_expanded

def FlimitDFS(board,limit, function, nodes_expanded):
    running = True
    min = 10000000
    open = deque()
    nodes_openned = nodes_expanded
    while running:
        cost = function(board) + board.moves_made
        if cost <= limit:
            if isSolved(board):
                return board.moves, nodes_openned
            for move in board.generateMoves():
                new_board = copy(board)
                new_board.makeMove(move)
                new_board.moves_made += 1
                new_board.moves.append(move)
                open.append(new_board)
                nodes_openned += 1
        else:
            if cost < min:
                min = cost

        if len(open) == 0:
            running = False
        else:
            board = open.pop()
    return min, nodes_openned

def isNumber(item):
    try:
        number_test = item - 1
        return True
    except TypeError:
        return False

def isSolved(board):
    return board.b == [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
