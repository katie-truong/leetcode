"""
dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)
"""

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        
        def dp(numDice, remainingTarget):
            if numDice == 0:
                return 0 if remainingTarget > 0 else 1
            if (numDice, remainingTarget) in memo:
                return memo[(numDice, remainingTarget)]
            val = 0
            for i in range(max(0, remainingTarget-f), remainingTarget):
                val += dp(numDice-1, i)
            memo[(numDice, remainingTarget)] = val
            return val
        
        return dp(d, target) % (10**9 + 7)
        
        
        