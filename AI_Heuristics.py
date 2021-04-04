import numpy as np, math
from copy import deepcopy
weight_table = [[1.5, 1, 0.5, 0],[2, 2.5, 3, 3.5],[7, 6, 5, 4],[8, 10, 12, 14]]
def heuristics(grid, num_empty):
  '''
  This function scores the grid based on the algorithm implemented
  so that the maximize function of AI_Minimax can decide which branch
  to follow.
  '''
  grid = np.array(grid)
  score = 0
  max_val = 0
  max_r, max_c = 0, 0
  # TODO: Implement your heuristics here. 
  # You are more than welcome to implement multiple heuristics
  
  #checking for monotonicity
  for i in range(len(grid)):
    for j in range(len(grid[i])):
        score += grid[i][j] * 2**weight_table[i][j]
        if grid[i][j] >= max_val:
            max_val = grid[i][j]
            max_r = i
            max_c = j
  
  # Weight for each score
  return score * num_empty / (max_val ** (6 - max_r - max_c))
