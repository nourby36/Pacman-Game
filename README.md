# Pac-Man Maze Navigation with A* Search Algorithm

This project implements a maze navigation game inspired by Pac-Man, where Pac-Man moves to multiple goal locations within a maze using the A* search algorithm. Static ghosts serve as obstacles, making the pathfinding challenge more complex.

## Features

- **Maze Navigation**: Uses the A* search algorithm to find the shortest path to each goal.
- **Obstacle Avoidance**: Avoids cells occupied by static ghost agents while navigating.
- **Path Visualization**: Visually traces Pac-Man's path to each goal with an animated delay.
- **Performance Metric**: Displays the search path length for each goal.

## Installation

To run this code, you need Python and the `pyamaze` package. Install it using:

```bash
pip install -r requirements.txt
```


## Usage

1. **Run the Code**: Execute the main script to visualize Pac-Man navigating through the maze toward each goal while avoiding ghost positions.

   ```python
   python pacman_maze.py
   ```

## Code Structure
- **aStar Function**: Implements the A* search algorithm to calculate the shortest path from Pac-Man’s current position to each goal position.
- **killAgent Function**: Removes agents from the maze once Pac-Man reaches a goal, keeping the visualization clean.
- **Ghost and Goal Setup**: Configures the starting positions of ghosts (obstacles) and goals in the maze. Each ghost acts as a static obstacle, and each goal is an objective for Pac-Man to reach.
