import random

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = 0
        self.square = self.square_number(row, column)
        self.editable = True

    def square_number(self, row, column):
        if row < 3 and column < 3:
            return 0
        elif row > 2 and row < 6 and column < 3:
            return 1
        elif row > 5 and column < 3:
            return 2
        elif row < 3 and column > 2 and column < 6:
            return 3
        elif row > 2 and row < 6 and column > 2 and column < 6:
            return 4
        elif row > 5 and column > 2 and column < 6:
            return 5
        elif row < 3 and column > 5:
            return 6
        elif row > 2 and row < 6 and column > 5:
            return 7
        elif row > 5 and column > 5:
            return 8
        else:
            return -1

class SudokuSolver:
    def __init__(self):
        self.Cell = [Cell(row, col) for row in range(9) for col in range(9)]

    def validate(self, value):
        return value.isdigit() and 1 <= int(value) <= 9

    def valid_check(self, cell, value):
        for c in self.Cell:
            if (c.row == cell.row or c.column == cell.column or c.square == cell.square) and c.value == value:
                return False
        return True

    def solve_sudoku(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i = 0
        n = 0
        m = 1

        while True:
            if i == 81:
                break
            if self.Cell[i].editable:
                if self.valid_check(self.Cell[i], numbers[n]):
                    self.Cell[i].value = numbers[n]
                    i += 1
                    n = 0
                    m = 1
                else:
                    if n == 8:
                        self.Cell[i].value = 0
                        i -= 1
                        m = 0
                        if self.Cell[i].value == 9:
                            i -= 1
                        n = self.Cell[i].value
                    else:
                        n += 1
            else:
                if m:
                    i += 1
                else:
                    i -= 1

    def import_puzzle(self):
        return [[0,0,0,2,6,0,7,0,1],
                [6,8,0,0,7,0,0,9,0],
                [1,9,0,0,0,4,5,0,0],
                [8,2,0,1,0,0,0,4,0],
                [0,0,4,6,0,2,9,0,0],
                [0,5,0,0,0,3,0,2,8],
                [0,0,9,3,0,0,0,7,4],
                [0,4,0,0,5,0,0,3,6],
                [7,0,3,0,1,8,0,0,0]]

    def load_sudoku(self):
        self.clear_gui()
        puzzle = self.import_puzzle()
        for c in range(9):
            for r in range(9):
                if puzzle[c][r] != 0:
                    self.Cell[c * 9 + r].value = puzzle[c][r]
                    self.Cell[c * 9 + r].editable = False

    def generate_sudoku(self):
        self.clear_gui()
        for cell in self.Cell:
            cell.editable = True
            cell.value = random.randint(1, 9) if random.random() < 0.6 else 0

    def clear_gui(self):
        for cell in self.Cell:
            cell.value = 0
            cell.editable = True

def main():
    solver = SudokuSolver()
    solver.generate_sudoku()
    print("Generated Sudoku:")
    sudoku_gui(solver)

    while True:
        command = input("Enter 'solve' to get the solution: ")
        if command.lower() == "solve":
            solver.solve_sudoku()
            print("\nSolved Sudoku:")
            sudoku_gui(solver)
            break
        else:
            print("Invalid command. Please enter 'solve' to get the solution.")

def sudoku_gui(solver):
    for row in range(9):
        for col in range(9):
            print(solver.Cell[row * 9 + col].value, end=" ")
        print()

if __name__ == "__main__":
    main()
