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
