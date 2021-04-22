from solution.algorithms.utils import *
from solution.algorithms.constants import *
import numpy as np

def find_princess(grid,n,start_row, start_column):
 dimensions = int(n)

 route_to_princess =[]

 visited = np.full((dimensions,dimensions), False)

 row_direction = [-1, 1, 0, 0]
 column_direction = [0, 0, 1, -1]
 found_princess = False

 coordinates_queue = [((start_row,start_column),[])]

 while coordinates_queue:
   row_column, found_route = coordinates_queue.pop(0)
   found_route.append(row_column)

   visited[row_column[0]][row_column[1]] = True

   if grid[row_column[0]][row_column[1]] == PRINCESS:
     found_princess = True

     route_to_princess = route_to_letters(found_route)
     print(route_to_princess)
     print(f'FOUND')
     break

   for direction in range(DIRECTIONS_TO_SEARCH):
     current_row = row_column[0] + row_direction[direction]
     current_column = row_column[1] + column_direction[direction]
     
     if current_row < 0 or current_column < 0:
       continue
     if current_row >= dimensions or current_column >= dimensions:
       continue
      
     if visited[current_row][current_column]:
       continue
     if grid[current_row][current_column] == OBSTICLES:
       continue

     coordinates_queue.append(((current_row,current_column),found_route[:]))

     visited[current_row][current_column] = True
 
 if found_princess:
     return route_to_princess
 return []
