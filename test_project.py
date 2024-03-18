from project import SudokuSolver

def test_generate_sudoku():
    solver = SudokuSolver()
    solver.generate_sudoku()
    assert len([cell for cell in solver.Cell if cell.value != 0]) >= 17

def test_solve_sudoku():
    solver = SudokuSolver()
    solver.load_sudoku()
    solver.solve_sudoku()
    assert all(cell.value != 0 for cell in solver.Cell)

def test_clear_gui():
    solver = SudokuSolver()
    solver.generate_sudoku()
    solver.clear_gui()
    assert all(cell.value == 0 for cell in solver.Cell)
