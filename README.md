# AI-Learning-Environments

This repository contains AI course projects curated by **Pouria Sameti (TA)** under the supervision of **Dr. Hossein Karshenas** at the University of Isfahan.
<br>
project phases covering key AI domains such as **Markov Decision Processes (MDP), Reinforcement Learning (RL), First-Order Logic (FOL), and Game Playing**. The repository is designed to support students' understanding of theoretical concepts through practical coding exercises and projects. Each section reflects the progression of the course and offers valuable insights for learning, experimentation, and further development in the field of AI.

### Table of Contents
- [MDP](https://github.com/pouriaSameti/AI-Learning-Environments?tab=readme-ov-file#markov-decision-processes)<br>
- [RL]()<br>
- [Game I]()<br>
- [Game II]()<br>
- [FOL]()<br>
------------------

## Markov Decision Processes
This project provides a flexible and modular environment based on the Markov Decision Process (MDP) paradigm. Students are tasked with implementing core reinforcement learning algorithms such as **value iteration, policy iteration, and Q-learning**. The environment includes stochastic transitions, intermediate states, and dynamic reward/penalty structures, encouraging students to explore various decision-making strategies.

### Objectives
- Gain hands-on experience with foundational RL algorithms in a controlled, stochastic setting.
- Experiment with reward shaping and penalties to influence agent behavior.
- Strategize and optimize policies to reach terminal states while satisfying cumulative score requirements.

### Environment Features
- The environment is an 8×8 grid world, where the agent (an "angry bird") starts at the top-left corner `(0, 0)` and aims to reach the bottom-right corner `(7, 7)` where the eggs are located. Reaching the eggs gives the agent `+400` reward points.<br>
- The agent can perform four actions: `up`, `down`, `left`, and `right`. However, the environment is **stochastic**:
  - Each action succeeds with a primary probability (e.g., 80%).
  - With the remaining probability, the agent might take one of the neighboring actions (e.g., 10% left, 10% right if the intended action is "up").<br>
  
- There are **8 pigs** randomly placed on the grid at each game run. Reaching a pig grants the agent `+250` reward points.<br>
- There are **2 queens**, also randomly placed in each game. Colliding with a queen results in a `-400` penalty.<br>
- The environment also includes **8 rocks** that act as obstacles. These are **randomly placed** and cannot be crossed by the agent.<br>
- Every move the agent makes (regardless of outcome) results in a `-1` step penalty, encouraging efficient pathfinding.

### Solution
To solve this project, follow these steps:
1. **Implement a reward function** to assign rewards to each target (e.g., pigs) and eggs in the environment. The output of this step should be a 3D tensor representing the reward map across different object types and positions.<br>

2. **Apply a planning algorithm**, such as value iteration or policy iteration. Using the generated reward maps for pigs and eggs, run the algorithm to derive an optimal policy for the agent.

### Installation
To run this project, install the required dependencies using the following commands:
```python
  pip install numpy
```
```python
  pip install pygame
```

> [!NOTE]
> A detailed **instruction PDF** is provided alongside the project files. This document explains the available environment functions and how to interact with them, guiding students in using the predefined interfaces to build and test their implementations.

![image](https://github.com/user-attachments/assets/13db9d72-354d-43eb-9df9-aeb013e68381)
----------

