"""
Project Title: Unknown Environment for Reinforcement Learning

Department:
    Artificial Intelligence Department
    Faculty of Computer Engineering
    University of Isfahan
    November 1, 2024

Supervisor:
    Dr. Hossein Karshenas(h.karshenas@eng.ui.ac.ir) - Professor
    Pouria Sameti(pouria.sameti2002@mehr.ui.ac.ir) - Teaching Assistant

Project Overview:
    This project involves designing an "Unknown Environment" where students will implement reinforcement learning
    algorithms such as SARSA and Q-learning. The environment is characterized by its stochastic nature, providing
    students with a platform to explore various strategies for effective learning and decision-making under uncertainty.

Objectives:
    - To enable students to gain hands-on experience with reinforcement learning algorithms.
    - To encourage experimentation with different approaches to handle the challenges presented by the unknown environment.
    - To foster a deeper understanding of key concepts in artificial intelligence and machine learning.

Licensing Information:
    -You are free to use or extend these projects for educational purposes.
"""


import numpy as np
import pygame
import random
import copy

#######################################################
#                DONT CHANGE THIS PART                #
#######################################################
COLORS = {
    'T': (245, 245, 220),    # Tile ground
    'P': (245, 245, 220),    # Pigs
    'Q': (245, 245, 220),    # Queen
    'G': (245, 245, 220),    # Goal
    'R': (245, 245, 220),    # Rock
    'TNT': (245, 245, 220),  # TNT
}

GOOD_PIG_REWARD = 250
GOAL_REWARD = 400
QUEEN_REWARD = (-400)
DEFAULT_REWARD = (-1)
TNT_REWARD = (-2000)
ACTION_TAKEN_REWARD = (-1000)

PIGS = 8
QUEENS = 2
ROCKS = 8
TNTs = 1
MAX_ACTIONS = 150

#######################################################
#                DONT CHANGE THIS PART                #
#######################################################
class PygameInit:

    @classmethod
    def initialization(cls):
        grid_size = 8
        tile_size = 100

        pygame.init()
        screen = pygame.display.set_mode((grid_size * tile_size, grid_size * tile_size))
        pygame.display.set_caption("Unknown Angry Birds")
        clock = pygame.time.Clock()

        return screen, clock


#######################################################
#                DONT CHANGE THIS PART                #
#######################################################
class UnknownAngryBirds:
    def __init__(self):
        self.__grid_size = 8
        self.__tile_size = 100
        self.__num_pigs = PIGS
        self.__num_queens = QUEENS
        self.__num_rocks = ROCKS
        self.__num_tnts = TNTs

        self.reward = 0
        self.done = False
        self.pig_states = []
        self.__pig_coordinates = []
        self.__base_grid = self.__generate_grid()
        self.__grid = copy.deepcopy(self.__base_grid)
        self.__probability_dict = self.__generate_probability_dict()

        self.__agent_pos = (0, 0)
        self.__max_actions = MAX_ACTIONS
        self.__actions_taken = 0

        self.__agent_image = pygame.image.load("Env/icons/yellow bird.png")
        self.__agent_image = pygame.transform.scale(self.__agent_image, (self.__tile_size, self.__tile_size))

        self.__pig_image = pygame.image.load('Env/icons/pigs.png')
        self.__pig_image = pygame.transform.scale(self.__pig_image, (self.__tile_size, self.__tile_size))
        self.__pig_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__pig_with_background.fill((245, 245, 220))
        self.__pig_with_background.blit(self.__pig_image, (0, 0))

        self.__yellow_bird = pygame.image.load('Env/icons/angry bird blue.png')
        self.__yellow_bird = pygame.transform.scale(self.__yellow_bird, (self.__tile_size, self.__tile_size))
        self.__yellow_bird_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__yellow_bird_with_background.fill((245, 245, 220))
        self.__yellow_bird_with_background.blit(self.__yellow_bird, (0, 0))

        self.__queen_image = pygame.image.load('Env/icons/queen.png')
        self.__queen_image = pygame.transform.scale(self.__queen_image, (self.__tile_size, self.__tile_size))
        self.__queen_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__queen_with_background.fill((245, 245, 220))
        self.__queen_with_background.blit(self.__queen_image, (0, 0))

        self.__rock_image = pygame.image.load('Env/icons/rocks.png')
        self.__rock_image = pygame.transform.scale(self.__rock_image, (self.__tile_size, self.__tile_size))
        self.__rock_with_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__rock_with_background.fill((245, 245, 220))
        self.__rock_with_background.blit(self.__rock_image, (0, 0))

        self.__tnt_image = pygame.image.load('Env/icons/TNT.png')
        self.__tnt_image = pygame.transform.scale(self.__tnt_image, (self.__tile_size, self.__tile_size))
        self.__tnt_background = pygame.Surface((self.__tile_size, self.__tile_size))
        self.__tnt_background.fill((245, 245, 220))
        self.__tnt_background.blit(self.__tnt_image, (0, 0))


    def __generate_grid(self):
        grid = [['T' for _ in range(self.__grid_size)] for _ in range(self.__grid_size)]

        while True:
            grid = [['T' for _ in range(self.__grid_size)] for _ in range(self.__grid_size)]
            filled_spaces = [(0, 0), (self.__grid_size - 1, self.__grid_size - 1)]

            num_holes = self.__num_pigs
            for _ in range(num_holes):
                while True:
                    r, c = random.randint(0, self.__grid_size - 1), random.randint(0, self.__grid_size - 1)
                    if (r, c) not in filled_spaces:
                        grid[r][c] = 'P'
                        filled_spaces.append((r, c))
                        self.__pig_coordinates.append((r, c))
                        break

            for _ in range(self.__num_queens):
                while True:
                    r, c = random.randint(0, self.__grid_size - 1), random.randint(0, self.__grid_size - 1)
                    if (r, c) not in filled_spaces:
                        grid[r][c] = 'Q'
                        filled_spaces.append((r, c))
                        break

            for _ in range(self.__num_rocks):
                while True:
                    r, c = random.randint(0, self.__grid_size - 1), random.randint(0, self.__grid_size - 1)
                    if (r, c) not in filled_spaces:
                        grid[r][c] = 'R'
                        filled_spaces.append((r, c))
                        break

            for _ in range(self.__num_tnts):
                while True:
                    r, c = random.randint(0, self.__grid_size - 1), random.randint(0, self.__grid_size - 1)
                    if (r, c) not in filled_spaces:
                        grid[r][c] = 'TNT'
                        filled_spaces.append((r, c))
                        break

            grid[self.__grid_size - 1][self.__grid_size - 1] = 'G'

            if UnknownAngryBirds.__is_path_exists(grid=grid, start=(0, 0), goal=(7, 7)):
                break
        return grid


    def reset(self):
        self.__grid = copy.deepcopy(self.__base_grid)
        self.__agent_pos = (0, 0)
        self.pig_states = []
        self.done = False
        self.__actions_taken = 0
        return self.__agent_pos
    

    @classmethod
    def __is_path_exists(cls, grid, start, goal):
        grid_size = len(grid)
        visited = set()

        def dfs(x, y):
            if (x, y) == goal:
                return True
            visited.add((x, y))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < grid_size and 0 <= ny < grid_size and
                        (nx, ny) not in visited and grid[nx][ny] != 'R'):
                    if dfs(nx, ny):
                        return True
            return False

        return dfs(start[0], start[1])


    def __generate_probability_dict(self):
        probability_dict = {}

        for row in range(self.__grid_size):
            for col in range(self.__grid_size):
                state = (row, col)
                probability_dict[state] = {}

                for action in range(4):
                    intended_prob = random.uniform(0.55, 0.90)
                    remaining_prob = 1 - intended_prob
                    neighbor_prob = remaining_prob / 2

                    probability_dict[state][action] = {
                        'intended': intended_prob,
                        'neighbor': neighbor_prob}
        return probability_dict

