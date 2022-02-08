import random
import copy

puzl_in = [ \
        [0,6,0,0,5,0,4,0,2],\
        [0,0,4,0,0,6,5,1,8],\
        [0,0,0,1,0,4,0,0,3],\
        [0,0,0,0,0,0,0,0,1],\
        [0,7,0,0,1,0,0,0,0],\
        [2,3,0,0,6,0,0,0,0],\
        [3,0,5,0,7,0,1,2,0],\
        [6,0,0,0,0,0,7,0,5],\
        [0,4,0,0,0,0,0,0,0]]

class Puzzle:
    def __init__(self):
        self.puzzle = [[[int(integer) for integer in range(1,10)] for x in range(0,9)] for i in range(0,9)]
        self.solved_in = 0
    def __str__(self):
        string = ''
        for row in self.puzzle:
            for item in row:
                for x in range(1,10):
                    if x in item:
                        string += str(x)
                    else:
                        string += " "
                string += '|'
            string += ("\n")
        return string
    def print_clean(self):
        for row in self.puzzle:
            print("|",end='')
            for col in row:
                if len(col) == 1:
                    print(str(col[0]), end='|')
                else:
                    print(" ", end='|')
            print("")
    def create_puzzle(self):
        #MANUAL INPUT
        '''
        rows = []
        for row in range(0,9):
            rows.append(str(input("row " + str(row) + ": ")))
        should_be = [list() for x in range(0,9)]

        for i in range(0,9):
            for j in range(0,9):
                should_be[i].append(int(rows[i][j]))
        '''
        #//


        # AUTO INPUT
        should_be = puzl_in
        #//
        for col in range(0,9):
            for row in range(0,9):
                if should_be[col][row] == 0:
                    continue
                else:
                    dinq = []
                    for index in range(0,9):
                        if int(self.puzzle[col][row][index]) == int(should_be[col][row]):
                            continue
                        else:
                            dinq.append(self.puzzle[col][row][index])
                    for item in dinq:
                        self.puzzle[col][row].remove(item)
    def check_squares(self):
        iter_blocks = [list() for x in range(0,9)]
        iterator = 0
        for row in range(0,3):
            three_rows = [0+(3*row),1+(3*row),2+(3*row)]
            for col in range(0,3):
                three_cols = [0+(3*col),1+(3*col),2+(3*col)]
                for i in range(0,9):
                    iter_blocks[iterator].append((three_rows[int(i/3)],three_cols[i%3]))
                iterator += 1
        for i in iter_blocks:
            set = []
            for row,col in i:
                item = self.puzzle[row][col]
                if len(item) == 1:
                    if item[0] in set:
                        return False
                    set.append(item[0])
        return True
    def check_rows(self):
        for row in self.puzzle:
            set = []
            for item in row:
                if len(item) == 1:
                    if item[0] in set:
                        return False
                    set.append(item[0])
        return True
    def check_cols(self):
        for col in range(0,9):
            set = []
            for row in range(0,9):
                cell = self.puzzle[row][col]
                if len(cell) == 1:
                    if cell[0] in set:
                        return False
                    set.append(cell[0])
        return True
    def clean_squares(self):
        iter_blocks = [list() for x in range(0,9)]
        iterator = 0
        for row in range(0,3):
            three_rows = [0+(3*row),1+(3*row),2+(3*row)]
            for col in range(0,3):
                three_cols = [0+(3*col),1+(3*col),2+(3*col)]
                for i in range(0,9):
                    iter_blocks[iterator].append((three_rows[int(i/3)],three_cols[i%3]))
                iterator += 1

        fixed = False
        for i in iter_blocks:
            set = []
            for row,col in i:
                item = self.puzzle[row][col]
                if len(item) == 1:
                    set.append(item[0])

            for row,col in i:
                item = self.puzzle[row][col]
                if len(item) > 1:
                    for already_set in set:
                        try:
                            item.remove(already_set)
                            fixed = True
                        except ValueError:
                            continue
        return fixed
    def clean_rows(self):
        fixed = False
        for row in self.puzzle:
            set = []
            for item in row:
                if len(item) == 1:
                    set.append(item[0])

            for item in row:
                if len(item) > 1:
                    for already_set in set:
                        try:
                            item.remove(already_set)
                            fixed = True
                        except ValueError:
                            continue
        return fixed
    def clean_cols(self):
        fixed = False
        for col in range(0,9):
            set = []
            for row in range(0,9):
                cell = self.puzzle[row][col]
                if len(cell) == 1:
                    set.append(cell[0])
            for row in range(0,9):
                cell = self.puzzle[row][col]
                if len(cell) > 1:
                    for already_set in set:
                        try:
                            cell.remove(already_set)
                            fixed = True
                        except ValueError:
                            pass
        return fixed

    def hard_solve(self):
        while self.clean_cols() or self.clean_rows() or self.clean_squares():
            continue
    def is_solved(self):
        for row in self.puzzle:
            for col in row:
                if len(col) == 1:
                    continue
                else:
                    return False
        return self.check_cols() and self.check_rows() and self.check_squares()
    def state_space_search(self,puzzle):
        if puzzle.is_solved():
            return puzzle
        else:
            for row in range(0,9):
                for col in range(0,9):
                    if len(puzzle.puzzle[row][col]) == 1:
                        continue
                    else:
                        for item in puzzle.puzzle[row][col]:
                            updated = copy.deepcopy(puzzle)
                            updated.puzzle[row][col] = [item]
                            #updated.solved_in = run + 1
                            if updated.check_cols() and updated.check_rows() and updated.check_squares():
                                updated.hard_solve()
                                if updated.check_cols() and updated.check_rows() and updated.check_squares():
                                    updated.solved_in += 1
                                    print("hard solved to ")
                                    updated.print_clean()
                                    if not (returned := self.state_space_search(updated)) == None:
                                        return returned
                        return None
    def report(self):
        print("rows: " + str(self.check_rows()))
        print("cols: " + str(self.check_cols()))
        print("squares: " + str(self.check_squares()))
        print("Solved in " + str(self.solved_in) + " iterations")



if __name__ == '__main__':
    this_puzzle = Puzzle()
    this_puzzle.create_puzzle()
    this_puzzle.hard_solve()

    print("THIS PUZZLE HARD SOLVED TO ")
    this_puzzle.print_clean()
    print()
    print()
    returned = this_puzzle.state_space_search(this_puzzle)
    print()
    print()
    returned.print_clean()
    returned.report()
