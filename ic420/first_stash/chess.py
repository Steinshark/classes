import pygame
import random
import string

class Board:
    def __init__(self):
        # [0][1] is A2 [7][7] is H8
        self.position = [\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None],\
                        [None,None,None,None,None,None,None,None]\
                        ]
    def move(self,pos1,pos2):
        file1, rank1 = self.translate(pos1)
        file2, rank2 = self.translate(pos2)

        old_piece = self.position[file2][rank1]
        self.position[file1][rank1] = None
        self.position[file2][rank2] = old_piece

    def place_piece(self,piece,pos):
        file, rank = self.translate(pos)
        self.position[file][rank] = piece

    def translate(self,pos):
        file = string.ascii_lowercase.index(pos[0])
        rank = int(pos[1]) - 1
        return int(file),int(rank)

    def piece_at(self,pos):
        file, rank = self.translate(pos)
        return self.position[file][rank]

    def legal_moves(self,piece):
        

    def get_index_of_piece(self,piece):
        for i in range(0,8):
            for j in range(0,8):
                if self.position[i][j] == piece:
                    return (i,j)
        return None


    def print(self):
        for file in reversed(range(0,8)):
            print("|",end='')
            for rank in range(0,8):
                piece = self.position[rank][file]
                if piece == None:
                    print("   ",end="")
                else:
                    print(" " + str(piece) + " ",end="")
                print("|",end='')
            print("")

class Piece:
    def __init__(self,img,piece,color):
        self.display_img = img
        self.piece = piece
        self.color = color

    def __str__(self):
        return self.piece[0]

        if piece == 'knight'
        if piece == 'bishop'
        if piece == 'rook'
        if piece == 'queen'
        if piece == 'king'




def main():
    board = Board()
    board.place_piece(Piece("blankimg","knight","white"),"a1")
    board.place_piece(Piece("blankimg","ops","white"),"e4")
    board.place_piece(Piece("blankimg","ops","black"),"h8")
    board.print()
main()
