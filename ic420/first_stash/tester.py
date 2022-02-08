from astar import *
from idastar import *
from Board import *
import copy
import pdb
import time

search = {
    'aStar': aStar,
    'idaStar' : idaStar,
}


if __name__ == "__main__":
    n = int(input("Enter scramble size: "))
    funStr = input("Enter search function: ")
    f = search[funStr]
    b1 = Board()
    b1.scramble(n)
    b2 = Board()
    time1 = time.time()
    p , n1  = f(b1, misplacedTiles)
    print(funStr + " ran in " + str(time.time()-time1)[:6] + " seconds")
    print(len(p))
    applyMoves(b1,p)
    print(b1==b2)
    b1 = Board()
    b1.scramble(n)
    time2 = time.time()
    p , n2  = f(b1, manhattanDistance)
    print(funStr + " ran in " + str(time.time()-time2)[:6] + " seconds")
    print(len(p))
    applyMoves(b1,p)
    print(b1==b2)
    print("n1:" + str(n1) + " vs. n2:" + str(n2))
    print(n1>=n2)
