from collections import deque

def treasure_island(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    d = -1
    q = deque([0])

    while len(q) > 0:
        d += 1
        size = len(q)
        while size > 0:
            curr = q.popleft()
            row = curr // cols
            col = curr % cols

            if row + 1 < rows and matrix[row+1][col] != 'X':
                if matrix[row+1][col] == '*':
                    return d+1
                else:
                    matrix[row+1][col] = 'X'
                    q.append((row+1)*cols + col)

            if row - 1 >= 0 and matrix[row-1][col] != 'X':
                if matrix[row-1][col] == '*':
                    return d+1
                else:
                    matrix[row-1][col] = 'X'
                    q.append((row-1)*cols + col)

            if col + 1 < rows and matrix[row][col + 1] != 'X':
                if matrix[row][col+1] == '*':
                    return d+1
                else:
                    matrix[row][col+1] = 'X'
                    q.append((row)*cols + col + 1)

            if col - 1 >= 0 and matrix[row][col - 1] != 'X':
                if matrix[row][col-1] == '*':
                    return d+1
                else:
                    matrix[row][col-1] = 'X'
                    q.append((row)*cols + col - 1)

        return -1


matrix1 = [[0, 0, 0, 0], ['X', 0, 'X', 0], [0, 0, 0, 0], [0, 'X', 'X', 'X']]
print(treasure_island(matrix1))