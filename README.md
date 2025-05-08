# AI-Learning-Environments

This repository contains AI course projects curated by **Pouria Sameti (TA)** under the supervision of **Dr. Hossein Karshenas** at the University of Isfahan.
<br>
project phases covering key AI domains such as **Markov Decision Processes (MDP), Reinforcement Learning (RL), First-Order Logic (FOL), and Game Playing**. The repository is designed to support students' understanding of theoretical concepts through practical coding exercises and projects. Each section reflects the progression of the course and offers valuable insights for learning, experimentation, and further development in the field of AI.

### Table of Contents
- [MDP](https://github.com/pouriaSameti/AI-Learning-Environments?tab=readme-ov-file#markov-decision-processes)<br>
- [RL](https://github.com/pouriaSameti/AI-Learning-Environments?tab=readme-ov-file#reinforcement-learning)<br>
- [Game I]()<br>
- [Game II]()<br>
- [FOL]()<br>
------------------

## Markov Decision Processes
This project provides a flexible and modular environment based on the Markov Decision Process (MDP) paradigm. Students are tasked with implementing core reinforcement learning algorithms such as **value iteration**, and **policy iteration**. The environment includes stochastic transitions, intermediate states, and dynamic reward/penalty structures, encouraging students to explore various decision-making strategies.

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
<br>

> [!NOTE]
> A detailed **instruction PDF** is provided alongside the project files. This document explains the available environment functions and how to interact with them, guiding students in using the predefined interfaces to build and test their implementations.

### Environment
![Screenshot 2025-05-08 163722](https://github.com/user-attachments/assets/12b09ea0-2885-46e9-a89a-a149f22188ab)

--------------------------
## Reinforcement learning
This project involves designing an "Unknown Environment" where students will implement reinforcement learning algorithms such as **SARSA and Q-learning**. The environment is characterized by its stochastic nature, providing students with a platform to explore various strategies for effective learning and decision-making under uncertainty.

### Objectives
- To enable students to gain hands-on experience with reinforcement learning algorithms.
- To encourage experimentation with different approaches to handle the challenges presented by the unknown environment.
- To foster a deeper understanding of key concepts in artificial intelligence and machine learning.

### Environment Features
- The environment is an 8×8 grid world, where the **agent (a yellow bird)** starts at the top-left corner `(0, 0)` and aims to reach a **blue bird** at the bottom-right corner `(7, 7)`. Reaching the blue bird grants `+400` points and ends the game.<br>

- The agent can perform four actions: `up`, `down`, `left`, and `right`. Every action results in a `-1` penalty, encouraging efficient movement.<br>

- The agent’s actions are **stochastic**:
  - the intended action (main action) is executed with a certain probability, while the remaining probability is split between two neighboring actions (side effects).
  - **Important**: These transition probabilities are not adjustable. They are **randomly generated by the environment** at the beginning and can be accessed via environment-provided functions.<br>

- There are **8 randomly placed obstacles** on the grid. The agent cannot pass through these cells.<br>
- There are **8 pigs** randomly placed on the grid. Colliding with a pig grants `+250` points and removes the pig from the environment.<br>
- There are **2 queen pigs**, which are also randomly placed. If the agent collides with a queen, it receives a `-400` penalty.<br>
- A single **TNT block** is placed randomly in the environment. Hitting it results in a `-2000` penalty and immediate termination of the episode.<br>
- The agent is allowed a maximum of **150 actions per episode**. If this limit is exceeded without reaching the goal, the agent receives a `-1000` penalty and the episode ends.


### Solution
To complete this project, follow these steps:

1. **Choose and implement a learning algorithm** (e.g., Q-learning) that allows the agent to interact with the unknown environment and derive a policy. You are encouraged to experiment with different algorithms and compare their performance.<br>

2. Unlike the previous project, the optimal policy cannot be learned in a single episode. The agent must go through **multiple episodes**, gradually updating its knowledge (e.g., a Q-table). After each episode, the updated Q-table should be saved and reused in the next run to enable learning over time.

3. To monitor the convergence of your algorithm, compute the **Value Difference** after each episode using the formula below:
   $$\text{Value Difference} = \sum_{s \in S} \sum_{a \in A} \left| Q^{(k+1)}(s, a) - Q^{(k)}(s, a) \right|$$<br> <br> This metric compares the Q-values before and after an update in a given episode. Store this value after each episode and plot it to visualize convergence. When the Value Difference drops below a small threshold (e.g., 0.01 or 0.001), the learning process can be considered converged.

4. **Visualize the learned policy** by creating an 8×8 map where each cell displays the action suggested by the final policy for that state.<br>
5. Finally, **allow the agent to act in the environment** using the converged policy from the learned Q-table to assess its performance.

> [!CAUTION]
> **The student should maintain multiple Q-tables, one for each target, and ensure that all these Q-tables converge.**

> [!NOTE]
> A detailed **instruction PDF** is provided alongside the project files. This document explains the available environment functions and how to interact with them, guiding students in using the predefined interfaces to build and test their implementations.

### Environment
![Screenshot 2025-05-08 170735](https://github.com/user-attachments/assets/d02eec7a-4ed3-4c5c-a153-75b8d123be45)

--------------------------
## Game I – Adversarial Search in Grid-Based Environment
This project introduces an interactive, **turn-based 10×10 grid** environment, where two Max player and the Min player compete under adversarial conditions. The goal is to **implement and test game tree algorithms such as Minimax**, possibly with heuristic enhancements. This environment includes **dynamic win/lose conditions**, various entities with different reward/penalty values, and **deterministic state transitions**. It provides an ideal setup for learning and evaluating optimal decision-making using adversarial search strategies.

### Objectives
- Implement Minimax search (with or without enhancements) to plan optimal actions for the Hen.<br>

- Develop a **heuristic evaluation function** to estimate the value of non-terminal states.
- Experiment with adversarial planning techniques and evaluate how your strategy performs across different scenarios.
- Analyze the behavior and effectiveness of Max (Hen) vs Min (Pig Queen) decision-making under constrained conditions.

### Environment Features

- The environment is a **10×10 grid** with two main players:
  - **Hen (Max agent)**: attempts to gather points and reach the slingshot.<br>
  - **Pig Queen (Min agent)**: tries to catch the Hen and prevent it from winning.

- Other static entities include:
  - **Eggs**: `+200` points when collected by the Hen.<br>
  - **Pigs**: `-200` points if the Hen eats them.<br>
  - **Rocks**: impassable obstacles for both players.<br>
  - **Slingshot**: reaching it grants the Hen +400 points and ends the game in a win.<br>
  - **Pig Queen**: if it catches the Hen, the game ends in a loss with -1000 points.<br>

- The Hen can perform four actions: `up`, `down`, `left`, and `right`. Each action results in a `-1` point penalty.<br>
- The Pig Queen also moves using the same four actions and tries to minimize the Hen's score by approaching it intelligently. It cannot interact with eggs or pigs.<br>
- Action order: In each turn, the **Hen moves first, followed by the Queen**.<br>
- The game is **deterministic—no stochastic transitions**.<br>
- The maximum number of **Hen moves is 150**. If the Hen does not reach the slingshot within this limit, the **game ends in a loss**.
- The environment has two modes:
  ```python
  env = AngryGame(template='simple')
  ```
  ```python
  env = AngryGame(template='hard')
  ```
  Your agent must be designed to succeed in both modes.

### Solution
To complete this project:
1. **Implement a heuristic evaluation function** for non-terminal states. This is crucial, especially in deep game trees where reaching a terminal state (win/loss) isn't always feasible within search limits.<br>

2. **Design a Minimax-based decision algorithm** that selects actions for the Hen based on the current game state.<br>
3. Use provided interaction functions from the environment to simulate and evaluate game outcomes.<br>
4. Your agent must be able to:
  + Accumulate enough points from eggs and the slingshot.
  + Avoid pigs and especially the Queen.
  + Plan moves with awareness of the Queen's future actions (i.e., adversarial reasoning).<br>

> [!NOTE]
> A detailed **instruction PDF** is provided alongside the project files. This document explains the available environment functions and how to interact with them, guiding students in using the predefined interfaces to build and test their implementations.

### Environment
![image](https://github.com/user-attachments/assets/ac778875-4cce-42cd-8cf6-a93f9497d459)
--------------------------
