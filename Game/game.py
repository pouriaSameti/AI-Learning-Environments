"""
Project Title: Game

Department:
    Artificial Intelligence Department
    Faculty of Computer Engineering
    University of Isfahan
    November 20, 2024

Supervisor:
    Dr. Hossein Karshenas(h.karshenas@eng.ui.ac.ir) - Professor
    Pouria Sameti(pouria.sameti2002@mehr.ui.ac.ir) - Teaching Assistant

Project Overview:
    This project involves the creation of an interactive game environment designed
    specifically to implement and test game tree algorithms such as Minimax. The
    environment simulates a 10x10 grid-based  game where various entities, including
    a hen, a queen, pigs, eggs, rocks, and a slingshot, interact dynamically.
    These entities introduce complex scenarios involving rewards, penalties, and
    decision-making challenges. The environment is implemented in Python using
    Pygame and features diverse rewards, and win/lose conditions, providing a rich
    testing ground for AI algorithms. By integrating game tree techniques,the project
    aims to analyze optimal decision-making under different game states.

Objectives:
    -Provide a platform for experimenting with game tree enhancements and extensions.
    -Evaluate the effectiveness of the algorithms in decision-making for various entities (e.g., Hen, Queen).
    -Implement game tree algorithms in the environment


Licensing Information:
    -You are free to use or extend these projects for educational purposes.
"""


import pygame
import heapq
import copy

#######################################################
#                DONT CHANGE THIS PART                #
#######################################################
COLORS = {
    'T': (143, 188, 143),    # Tile ground
    'Q': (143, 188, 143),    # Queen
    'R': (143, 188, 143),    # Rock
    'H': (143, 188, 143),    # Hen
    'E': (143, 188, 143),    # Egg
    'S': (143, 188, 143),    # slingshot
    'P': (143, 188, 143)     # Pigs
}

EGG_REWARD = 200
PIG_REWARD = -200
DEFAULT_REWARD = (-1)
LOSE_REWARD = -1000
SLING_REWARD = 400

EGGS = 8
PIGS = 8
QUEEN = 1

MAX_ACTIONS = 150

#######################################################
#                DONT CHANGE THIS PART                #
#######################################################


class PygameInit:

    @classmethod
    def initialization(cls):
        grid_size_x = 10
        grid_size_y = 10
        tile_size = 80

        pygame.init()
        screen = pygame.display.set_mode((grid_size_x * tile_size, grid_size_y * tile_size))
        pygame.display.set_caption("GAME")
        clock = pygame.time.Clock()

        return screen, clock
