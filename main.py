# Name: Courtney Vu
# Date: 05/08/2025
# Description: Main file for the Sudoku Solver game

import pygame
from game import SudokuGame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoku Solver")

    # Create game instance
    game = SudokuGame(screen)
    running = True

    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_input(event)

        game.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main() 