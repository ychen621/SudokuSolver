# Global variables
import sys
import heapq
from dataclasses import dataclass, field
from typing import List, Tuple

row = 9
column = 9
valid = False

@dataclass(order=True)
class Node:
    """
        The dataclass is imported to allow heapq(priority queue) to work
        The default value for compare of each field is True; however, we only want the heapq sorts the Node based on length
        Therefore, the compare value of domain and coordinates are set to be False
    """
    length: int
    domain: set = field(compare=False)
    coordinates: tuple = field(compare=False)

'''
    Read Sudoku Input File
    - First Line should contain the title and level
    - Line 2 - 10 is the Sudoku Matrix
'''
def read_file(filename):

    matrix = [[0 for x in range(row)] for y in range(column)]

    with open(filename) as file:
        title = next(file)
        r = 0

        while True:
            line = file.readline()
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
    Find the valid number for the given cell
    - Check the same row
    - Check the same column
    - Check the same 3*3 block
'''
def find_valid(matrix, r, c):
    full_domain = set(range(1, 10))
    row_domain = set(matrix[r])
    col_domain = {matrix[n][c] for n in range(row)}
    grid_domain = set()
    r_section = r//3
    c_section = c//3
    for i in range(r_section*3, r_section+3):
        for j in range(c_section*3, c_section+3):
            grid_domain.add(matrix[i][j])

    return full_domain.difference(row_domain | col_domain | grid_domain)

def mrv_indices(matrix):
    heap = list()
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                node_domain = find_valid(matrix, i, j)
                heapq.heappush(heap, Node(len(node_domain), node_domain, (i, j)))
    node = heapq.heappop(heap)
    return node.coordinates[0], node.coordinates[1], node.domain

def check_number(r, c, num, matrix):
    for i in range(9):
        if matrix[r][i] == num or matrix[i][c] == num:
            return False

    r_section = r//3
    c_section = c//3
    for i in range(r_section*3, r_section+3):
        for j in range(c_section*3, c_section+3):
            if matrix[i][j] == num:
                return False
    return True

def backtracking(matrix):
    need_update = False
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                need_update = True
                break
        if need_update: break

    if not need_update:
        print("Answer for the Sudoku - Simple Backtracking Algorithm: ")
        for line in matrix:
            print(line)
        exit(0)

    i, j, domain = mrv_indices(matrix)
    for num in domain:
        if check_number(i, j, num, matrix):
            matrix[i][j] = num
            if backtracking(matrix):
                return True
            matrix[i][j] = 0
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
