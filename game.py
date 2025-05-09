# Name: Courtney Vu
# Date: 05/08/2025
# Description: Game logic for the Sudoku Solver game

from enum import Enum
from typing import List
import pygame
from constants import GRID_SIZE, DEFAULT_GRID
from ui import UI

class GameState(Enum):
    PLAYING = 1
    SOLVING = 2
    SOLVED = 3
    ERROR = 4

class SudokuGame:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.ui = UI(screen)
        self.grid = self._create_default_grid()
        self.selected_cell = (0, 0)
        self.game_state = GameState.PLAYING
        self.error_message = ""

    def _create_default_grid(self) -> List[List[int]]:
        return [row[:] for row in DEFAULT_GRID]

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """Check if a number is valid in the given position."""
        # Check row
        for x in range(GRID_SIZE):
            if self.grid[row][x] == num:
                return False

        # Check column
        for x in range(GRID_SIZE):
            if self.grid[x][col] == num:
                return False

        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve(self, row: int = 0, col: int = 0) -> bool:
        """Solve the Sudoku puzzle using backtracking."""
        if row == GRID_SIZE - 1 and col == GRID_SIZE:
            return True

        if col == GRID_SIZE:
            row += 1
            col = 0

        if self.grid[row][col] > 0:
            return self.solve(row, col + 1)

        for num in range(1, GRID_SIZE + 1):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                self.selected_cell = (row, col)
                self.draw()
                pygame.display.update()
                pygame.time.delay(20)

                if self.solve(row, col + 1):
                    return True

                self.grid[row][col] = 0
                self.draw()
                pygame.display.update()
                pygame.time.delay(50)

        return False

    def handle_input(self, event: pygame.event.Event):
        """Handle user input events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.selected_cell = self.ui.get_cell_from_pos(event.pos)
        elif event.type == pygame.KEYDOWN:
            self._handle_keydown(event.key)

    def _handle_keydown(self, key: int):
        """Handle keyboard input."""
        x, y = self.selected_cell
        
        if key == pygame.K_LEFT and x > 0:
            self.selected_cell = (x - 1, y)
            self.error_message = ""
        elif key == pygame.K_RIGHT and x < GRID_SIZE - 1:
            self.selected_cell = (x + 1, y)
            self.error_message = ""
        elif key == pygame.K_UP and y > 0:
            self.selected_cell = (x, y - 1)
            self.error_message = ""
        elif key == pygame.K_DOWN and y < GRID_SIZE - 1:
            self.selected_cell = (x, y + 1)
            self.error_message = ""
        elif pygame.K_1 <= key <= pygame.K_9:
            num = key - pygame.K_1 + 1
            if self.is_valid_move(x, y, num):
                self.grid[x][y] = num
                self.error_message = ""
            else:
                self.error_message = "Invalid move!"
        elif key == pygame.K_RETURN:
            self.game_state = GameState.SOLVING
            if not self.solve():
                self.error_message = "No solution exists!"
                self.game_state = GameState.ERROR
            else:
                self.game_state = GameState.SOLVED
                self.error_message = ""
        elif key == pygame.K_r:
            self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
            self.game_state = GameState.PLAYING
            self.error_message = ""
        elif key == pygame.K_d:
            self.grid = self._create_default_grid()
            self.game_state = GameState.PLAYING
            self.error_message = ""

    def draw(self):
        """Draw the game state."""
        self.screen.fill((255, 255, 255))
        self.ui.draw_grid(self.grid)
        self.ui.draw_selected_cell(self.selected_cell)
        self.ui.draw_instructions()
        self.ui.draw_error_message(self.error_message) 