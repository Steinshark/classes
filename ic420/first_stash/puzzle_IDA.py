def populate(puzzle):
    string = input()
    letter_list = []
    for letter in string:
        letter_list.append(int(letter))

    for i in range(0,3):
        for j in range(0,3):
            puzzle[i][j] = letter_list[(i*3)+(j)]
    return puzzle

def get_manhattan(puzzle):
    sum = 0
    for row in range(0,3):
        for col in range(0,3):
            sum += get_distance(puzzle[row][col],row,col)
    return str(sum)

def get_distance(number, row, col):
    solved = [[0,1,2],[3,4,5],[6,7,8]]
    real_row, real_col = (0,0)
    iter = 0
    for row_check in solved:
        if number in row_check:
            real_row = iter
            real_col = row_check.index(number)
            break
        iter = iter + 1
    return abs(row-real_row) + abs(col-real_col)



puzzle = [[0,0,0],[0,0,0],[0,0,0]]
puzzle = populate(puzzle)

print("dist: " + get_manhattan(puzzle))
