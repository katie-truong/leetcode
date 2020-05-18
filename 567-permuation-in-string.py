class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        
        for char in s1:
            if char not in d:
                d[char] = 0
            d[char] += 1
            
        left = 0
        right = 0
        
        currChars = {}
        
        while right < len(s2):
            currRight = s2[right]
            if currRight in d:
                # Add right char into currChars dict
                if currRight not in currChars:
                    currChars[currRight] = 0
                currChars[currRight] += 1
                # If the count of an element is currChars is bigger than count in d,
                # move left to the right 
                if currChars[currRight] > d[currRight]:
                    while currChars[currRight] > d[currRight]:
                        currChars[s2[left]] -= 1
                        left += 1
                # If len of string is longer than p, remove first elem in the string
                while (right - left) > len(s1):
                    currLeft = s2[left]
                    left += 1
                    currChars[currLeft] -= 1
                # If currChars == d, s[left:right] is an anagram of p
                if currChars == d:
                    return True
                right += 1
            else:
                currChars = {}
                left = right + 1
                right += 1
                
        return False
            
            
            
            
        