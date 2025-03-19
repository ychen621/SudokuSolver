# Sudoku Solver

## Installation
1. Open terminal
2. Change the current working directory to your desired directory
3. Clone the repository
    ```console
    git clone https://github.com/ychen621/SudokuSolver.git
    ```
4. Press Enter to create your local clone

## Sudoku File Example
- File name: my_sudoku.txt
- File format
    ```text
    MySudoku hard
    003020600
    900305001
    001806400
    008102900
    700000008
    006708200
    002609500
    800203009
    005010300
    ```
- Note:
  - The first line should contain the question name and the level of question
    - Example: [mysudoku hard]
  - Starting from line 2 to line 10 is the matrix of your sudoku
    - 0 represents the empty block
    - 1 - 9 are the valid existing numbers

## Run program
### Simple Solver - Backtracking Algorithm
- Run command:
    ```console
    Python3 simpleSolver.py <sudoku_file_name>
    ```
### Advanced Solver - Minimum Remaining Value (MRV) + Backtracking
- For more advanced (faster) approach, use the mrvSolver
- Run command:
    ```console
    Python3 mrvSolver.py <sudoku_file_name>
    ```
- MRV uses priority queue (Heap) to sort the cell by numbers of remaining possible value for that cell.
- The cell with less possible value will be tested first to reduce the testing times 
