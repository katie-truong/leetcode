'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

def permute(nums):
    if not nums:
        return []
    result = []

    def backtrack(runningChoice):
        if len(runningChoice) == len(nums):
            result.append(runningChoice)
        else:
            for num in nums:
                if num in runningChoice:
                    continue
                runningChoice.append(num)
                backtrack(runningChoice)
                runningChoice.pop()

    backtrack([])

    return result
