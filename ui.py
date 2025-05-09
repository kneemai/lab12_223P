# Name: Courtney Vu
# Date: 05/08/2025
# Description: UI for the Sudoku Solver game

import pygame
from typing import Tuple
from constants import COLORS, WINDOW_WIDTH, CELL_SIZE, GRID_SIZE

class UI:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font1 = pygame.font.SysFont("times new roman", 30)
        self.font2 = pygame.font.SysFont("times new roman", 20)

    def draw_grid(self, grid: list[list[int]]):
        """Draw the Sudoku grid and numbers."""
        # Draw numbers
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if grid[i][j] != 0:
                    pygame.draw.rect(self.screen, COLORS['BLUE'],
                                   (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE + 1, CELL_SIZE + 1))
                    text = self.font1.render(str(grid[i][j]), 1, COLORS['BLACK'])
                    cell_center_x = i * CELL_SIZE + CELL_SIZE / 2
                    cell_center_y = j * CELL_SIZE + CELL_SIZE / 2
                    text_x = cell_center_x - text.get_width() / 2
                    text_y = cell_center_y - text.get_height() / 2
                    self.screen.blit(text, (text_x, text_y))

        # Draw grid lines
        for i in range(GRID_SIZE + 1):
            thick = 5 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, COLORS['BLACK'],
                           (0, i * CELL_SIZE), (WINDOW_WIDTH, i * CELL_SIZE), thick)
            pygame.draw.line(self.screen, COLORS['BLACK'],
                           (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_WIDTH), thick)

    def draw_selected_cell(self, selected_cell: Tuple[int, int]):
        """Highlight the currently selected cell."""
        x, y = selected_cell
        for i in range(2):
            pygame.draw.line(self.screen, COLORS['RED'], 
                           (x * CELL_SIZE - 3, (y + i) * CELL_SIZE),
                           (x * CELL_SIZE + CELL_SIZE + 3, (y + i) * CELL_SIZE), 7)
            pygame.draw.line(self.screen, COLORS['RED'],
                           ((x + i) * CELL_SIZE, y * CELL_SIZE),
                           ((x + i) * CELL_SIZE, y * CELL_SIZE + CELL_SIZE), 7)

    def draw_instructions(self):
        """Draw game instructions."""
        text1 = self.font2.render("Press D to set to Default/ R to Reset", 1, COLORS['BLACK'])
        text2 = self.font2.render("Enter values and press Enter to solve", 1, COLORS['BLACK'])
        self.screen.blit(text1, (20, 510))
        self.screen.blit(text2, (20, 530))

    def draw_error_message(self, error_message: str):
        """Draw error message."""
        if error_message:
            text = self.font1.render(error_message, 1, COLORS['BLACK'])
            text_x = (WINDOW_WIDTH - text.get_width()) // 2
            self.screen.blit(text, (text_x, 565))

    def get_cell_from_pos(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """Convert mouse position to grid coordinates."""
        x = pos[0] // CELL_SIZE
        y = pos[1] // CELL_SIZE
        return (x, y) 