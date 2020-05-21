class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = matrix
        
        count = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 1:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    
        result = 0
        
        for r in range(m):
            result += sum(dp[r])
            
        return result