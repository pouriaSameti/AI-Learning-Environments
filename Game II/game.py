"""
Project Title: Game II

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
    a hen, a bird, a queen,pigs, eggs, rocks, and a slingshot, interact dynamically.
    These entities introduce complex scenarios involving rewards, penalties, and
    decision-making challenges. The environment is implemented in Python using
    Pygame and features diverse rewards, and win/lose conditions, providing a rich
    testing ground for AI algorithms. By integrating game tree techniques,the project
    aims to analyze optimal decision-making under different game states.

Objectives:
    -Provide a platform for experimenting with game tree enhancements and extensions.
    -Evaluate the effectiveness of the algorithms in decision-making for various entities (e.g., Hen, Bird, Queen).
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
    'B': (143, 188, 143),    # Red Bird
    'E': (143, 188, 143),    # Egg
    'S': (143, 188, 143),    # slingshot
    'P': (143, 188, 143)     # Pigs
}

EGG_REWARD = 200
PIG_REWARD = -200
DEFAULT_REWARD = (-1)
LOSE_REWARD = -1000
SLING_REWARD = 250
CATCH_QUEEN = 600

EGGS = 8
PIGS = 8
QUEEN = 1

MAX_ACTIONS = 200

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
        pygame.display.set_caption("GAME II")
        clock = pygame.time.Clock()

        return screen, clock

#######################################################
#                DONT CHANGE THIS PART                #
#######################################################
class AngryGame:
    def __init__(self, template: str):
        self.__grid_size = 10
        self.__tile_size = 80
        self.__template_type = template

        self.__base_grid = self.__generate_grid()
        self.grid = copy.deepcopy(self.__base_grid)
        self.__base_grid = copy.deepcopy(self.grid)

        self.num_actions = 0

        self.__hen_image = pygame.image.load("Env/icons/white bird.png")
        self.__hen_image = pygame.transform.scale(self.__hen_image, (self.__tile_size, self.__tile_size))

        self.__bird_image = pygame.image.load('Env/icons/angry-bird.png')
        self.__bird_image = pygame.transform.scale(self.__bird_image, (self.__tile_size, self.__tile_size))
        self.__bird_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__bird_with_background.fill((143, 188, 143))
        self.__bird_with_background.blit(self.__bird_image, (0, 0))

        self.__queen_image = pygame.image.load('Env/icons/queen.png')
        self.__queen_image = pygame.transform.scale(self.__queen_image, (self.__tile_size, self.__tile_size))
        self.__queen_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__queen_with_background.fill((143, 188, 143))
        self.__queen_with_background.blit(self.__queen_image, (0, 0))

        self.__pig_image = pygame.image.load('Env/icons/pig.png')
        self.__pig_image = pygame.transform.scale(self.__pig_image, (self.__tile_size, self.__tile_size))
        self.__pig_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__pig_with_background.fill((143, 188, 143))
        self.__pig_with_background.blit(self.__pig_image, (0, 0))

        self.__egg = pygame.image.load('Env/icons/egg.png')
        self.__egg = pygame.transform.scale(self.__egg, (self.__tile_size, self.__tile_size))
        self.__egg_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__egg_with_background.fill((143, 188, 143))
        self.__egg_with_background.blit(self.__egg, (0, 0))

        self.__rock_image = pygame.image.load('Env/icons/rocks.png')
        self.__rock_image = pygame.transform.scale(self.__rock_image, (self.__tile_size, self.__tile_size))
        self.__rock_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__rock_with_background.fill((143, 188, 143))
        self.__rock_with_background.blit(self.__rock_image, (0, 0))

        self.__slingshot_image = pygame.image.load('Env/icons/slingshot.png')
        self.__slingshot_image = pygame.transform.scale(self.__slingshot_image, (self.__tile_size, self.__tile_size))
        self.__slingshot_image_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__slingshot_image_background.fill((143, 188, 143))
        self.__slingshot_image_background.blit(self.__slingshot_image, (0, 0))
    
    def __generate_grid(self):

        grid = [['T' for _ in range(self.__grid_size)] for _ in range(self.__grid_size)]

        with open(f'Env/templates/{self.__template_type}.txt') as file:
            template_str = file.readlines()

        for i in range(self.__grid_size):
            for j in range(self.__grid_size):
                grid[i][j] = template_str[i][j]

        return grid

    def reset(self):
        self.grid = copy.deepcopy(self.__base_grid)
        self.num_actions = 0

    @classmethod
    def print_grid(cls, grid):
        printed_grid = ''

        for r in range(len(grid)):
            printed_grid += '\n'
            for c in range(len(grid)):
                printed_grid += grid[r][c]

        return printed_grid + '\n'