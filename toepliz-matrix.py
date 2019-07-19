"""
Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
isn’t a Toeplitz matrix, so we should return false.
"""

def isToeplitz(matrix):
  """
  @param arr: int[][]
  @return: bool
  """
  rows = len(matrix)
  cols = len(matrix[0])
  for x in range(rows-1):
    for y in range(cols-1):
      if matrix[x+1][y+1] != matrix[x][y]:
        return False
      else:
        continue
  return True
