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

