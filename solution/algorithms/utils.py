from solution.algorithms.constants import *

def route_to_letters(found_route):
     moves = []
     for i in range(len(found_route)-1):
       if found_route[i][0] < found_route[i+1][0] and found_route[i][1] == found_route[i+1][1]:
         moves.append('DOWN')
       if found_route[i][0] > found_route[i+1][0] and found_route[i][1] == found_route[i+1][1]:
         moves.append('UP')
       if found_route[i][0] == found_route[i+1][0] and found_route[i][1] > found_route[i+1][1]:
         moves.append('LEFT')
       if found_route[i][0] == found_route[i+1][0] and found_route[i][1] < found_route[i+1][1]:
         moves.append('RIGHT')
     return moves

def find_marion_position(matrix):
    for r, matrix_r in enumerate(matrix):
        for c, value in enumerate(matrix_r):
            if value == MARIO:
                return (r, c)

def validate_grid(n,grid):
  free_spots_count = grid.count(FREE_SPOTS)
  mario_count = grid.count(MARIO)
  princess_count = grid.count(PRINCESS)
  obsticles_count = grid.count(OBSTICLES)

  grid_size = free_spots_count + mario_count + princess_count + obsticles_count

  if mario_count == 1 and princess_count == 1:
      return grid_size == int(n)*int(n)
  return False

def to_matrix(array):
  mat = []
  for row in array:
    mat.append(row)
  return mat