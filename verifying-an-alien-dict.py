# Leetcode 953 

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        
        for i, char in enumerate(order):
            d[char] = i
            
        def valid(a, b):
            pointer = 0
            n = min(len(a), len(b))
            while pointer < n:
                if d[a[pointer]] < d[b[pointer]]:
                    return True
                elif d[a[pointer]] > d[b[pointer]]:
                    print(a[pointer], b[pointer])
                    return False
                pointer += 1
            return False if (len(a) > len(b)) else True
        
        for i in range(1, len(words)):
            if not valid(words[i-1], words[i]):
                print(words[i-1], words[i])
                return False
            
        return True