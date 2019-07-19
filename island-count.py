"""
Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

Example:

input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.

"""

def get_number_of_islands(matrix):
  total = 0
  rows = len(matrix)
  cols = len(matrix[0])
  
  for i in range(rows):
    for j in range(cols):
      if matrix[i][j] == 1:
        if i == rows - 1 and j == cols - 1:
          total += 1
        elif i == rows - 1 and j != cols - 1:
          if matrix[i][j+1] == 1:
            continue
          else:
            total += 1
        elif j == cols - 1:
          if matrix[i+1][j] == 1 or matrix[i+1][j-1] == 1:
            continue
          else:
            total += 1
        elif j == 0:
          if matrix[i][j+1] == 1 or matrix[i+1][j] == 1:
            continue
          else:
            total +=1
        else:
          if matrix[i][j+1] == 1 or matrix[i+1][j] == 1:
            continue
          elif matrix[i+1][j-1] == 1:
            if matrix[i][j-1] == 1:
              continue
            else:
              total += 1
          else:
            total += 1
            
  return total

 