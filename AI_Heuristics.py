import numpy as np, math
from copy import deepcopy
def heuristics(grid, num_empty):
  '''
  This function scores the grid based on the algorithm implemented
  so that the maximize function of AI_Minimax can decide which branch
  to follow.
  '''# TODO: Implement your heuristics here.
  # You are more than welcome to implement multiple heuristics
  
  grid = np.array(grid)
    
  #checking that the largest tile is bottom right
  max_val = 0
  max_r, max_c = 0, 0
  large_tile_penalty = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] >= max_val:
            max_val = grid[i][j]
            max_r = i
            max_c = j
  large_tile_penalty = 6 - max_r - max_c
  
  # checking monotonicity
  # check that it's increasing from left to right
  score = 0
  for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
      if(grid[i][j] > grid[i][j + 1]):
        score -= 1
      else:
        score += 1

  # check that it's increasing from top to bottom
  for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
      if(grid[j][i] > grid[j + 1][i]):
        score -= 1
      else:
        score += 1
        
  # check smoothness
  smoothness = 0
  return score - large_tile_penalty + smoothness + num_empty
