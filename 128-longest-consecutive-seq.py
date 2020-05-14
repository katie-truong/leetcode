# Take 1: O(range(min(nums), max(nums)))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set()
        for num in nums:
            numSet.add(num)
        currSeq = 1
        maxSeq = 1
        for i in range(min(nums) + 1, max(nums) + 1):
            if i in numSet and (i-1) in numSet:
                currSeq += 1
            else:
                maxSeq = max(maxSeq, currSeq)
                currSeq = 1
        maxSeq = max(maxSeq, currSeq)
        return maxSeq

# Take 2: DFS
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        seen = set()
        
        maxSeq = 0
        
        def dfs(num, currSeq):
            nonlocal maxSeq 
            nonlocal seen
            
            if num not in numSet:
                return 
            
            seen.add(num)
            
            currSeq += 1
            maxSeq = max(maxSeq, currSeq)
            
            dfs(num + 1, currSeq)
        
        for elem in numSet:
            if elem not in seen:
                dfs(elem, 0)
                
        return maxSeq
            
# Take 3: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        
        currSeq = 1
        curr = 0
        maxSeq = 1
        
        for num in numSet:
            if (num-1) not in numSet:
                curr = num
                currSeq = 1
            
            while (curr + 1) in numSet:
                curr += 1
                currSeq += 1
                    
            maxSeq = max(maxSeq, currSeq)
        
        return maxSeq