# Global variables
import sys

row = 9
column = 9
valid = False

# Read Sudoku Input File
def read_file(filename):
    # Input sudoku will be stored here
    matrix = [[0 for x in range(row)] for y in range(column)]

    # Read input file
    with open(filename) as file:

        # First line is the title
        title = next(file)
        r = 0

        # Start reading sudoku question input
        while True:
            line = file.readline()
            # Why 10 -> each line contains net line char
            if len(line) != 10:
                break
            c = 0
            for char in line:
                matrix[r][c] = int(char)
                c += 1
                if c==9:
                    r += 1
                    break
            if r==9:
                global valid
                valid = True
                break

    return matrix

'''
    Check if the given number is valid for this slot
    1. check whether the same row contains same number
    2. check whether the same col contains same number
    3. check whether the belonging 3*3 block contains the same number
'''
def check_number(r, c, num, matrix):

    invalid = False

    for i in range(9):
        if invalid:
            break
        if matrix[r][i] == num:
            invalid = True
        if matrix[i][c] == num:
            invalid = True

    r_section = r//3
    c_section = c//3
    if not invalid:
        for i in range(r_section*3, r_section+3):
            for j in range(c_section*3, c_section+3):
                if matrix[i][j] == num:
                    invalid = True
                    break
    return invalid


def backtracking(matrix):
    need_update = False
    r = 0
    c = 0
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                r = i
                c = j
                need_update = True

    if not need_update:
        print("Answer for the Sudoku - Simple Backtracking Algorithm: ")
        for line in matrix:
            print(line)
        exit(0)

    for i in range(1, 10):
        if not check_number(r, c, i, matrix):
            matrix[r][c] = i
            if backtracking(matrix):
                return True
            matrix[r][c] = 0
    return False

if __name__ == "__main__":
    file = sys.argv[1]
    matrix = read_file(file)
    if not valid:
        print("Invalid sudoku file format")
        exit(0)

    print("Input sudoku: ")
    for line in matrix:
        print(line)

    backtracking(matrix)
