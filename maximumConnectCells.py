matrix1 = [
  [0, 1, 1, 2, 2],
  [0, 0, 1, 2, 1],
  [0, 0, 1, 2, 1],
  [0, 1, 1, 0, 1],
  [2, 1, 2, 1, 0]
]

matrix2 = [
  [1, 2],
  [1, 0]
]

def find(matrix):
  m = len(matrix)
  n = len(matrix[0])

  maxSum = 0

  visited = set()

  MOVES = {(-1,0), (1,0), (0,-1), (0,1)}

  def valid(r, c):
    return 0 <= r < m and 0 <= c < n 

  def dfs(r, c, num):
    nonlocal maxSum
    if not valid(r, c) or (r,c) in visited:
      maxSum = max(maxSum, num)
      return
    num += 1
    visited.add((r, c))
    for move in MOVES:
      new_r = r + move[0]
      new_c = c + move[1]
      if valid(new_r, new_c):
        if matrix[r][c] == matrix[new_r][new_c]:
          dfs(new_r, new_c, num)

  for r in range(m):
    for c in range(n):
      if (r, c) not in visited:
        dfs(r, c, 0)

  return maxSum

print(find(matrix1))