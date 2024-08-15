import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.f = None
        self.g = None
        self.h = None

random_maze = np.random.randint(2, size=(10, 10))

empty_maze = np.zeros((10, 10))

maze01 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],])


def visualize_maze(maze, maze_title):
    plt.figure(figsize=(5, 5))
    plt.imshow(maze, cmap='binary', interpolation='none')
    plt.grid(color='gray', linestyle='-', linewidth=2)
    plt.xticks(np.arange(-0.5, maze.shape[1], 1), [])
    plt.yticks(np.arange(-0.5, maze.shape[0], 1), [])  
    plt.tick_params(axis='both', which='both', length=0)  
    plt.title(maze_title)

    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_linewidth(3)
        spine.set_edgecolor('dimgray')


    plt.show()

# Visualize the maze
visualize_maze(maze01, "Test Maze")