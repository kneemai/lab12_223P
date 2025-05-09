# Name: Courtney Vu
# Date: 05/08/2025
# Description: Constants for the Sudoku Solver game

# Window and grid settings
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 610
GRID_SIZE = 9
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE

# Colors
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'BLUE': (70, 131, 188)
}

# Default grid
DEFAULT_GRID = [
    [2, 0, 0, 0, 0, 1, 0, 0, 5],
    [0, 0, 0, 7, 0, 5, 4, 6, 8],
    [5, 0, 0, 0, 6, 0, 0, 0, 1],
    [0, 8, 0, 9, 0, 4, 0, 0, 7],
    [0, 5, 0, 2, 0, 6, 1, 0, 4],
    [0, 3, 0, 5, 0, 0, 0, 0, 0],
    [6, 0, 4, 0, 7, 2, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 7, 8, 0],
    [0, 0, 0, 0, 0, 3, 2, 0, 0]
] 