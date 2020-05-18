class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        result = []
        
        d = {}
        for char in p:
            if char not in d:
                d[char] = 0
            d[char] += 1
            
        left = 0
        right = 0
        
        currChars = {}
        
        while right < len(s):
            currRight = s[right]
            if currRight in d:
                # Add right char into currChars dict
                if currRight not in currChars:
                    currChars[currRight] = 0
                currChars[currRight] += 1
                # If the count of an element is currChars is bigger than count in d,
                # move left to the right 
                if currChars[currRight] > d[currRight]:
                    while currChars[currRight] > d[currRight]:
                        currChars[s[left]] -= 1
                        left += 1
                # If len of string is longer than p, remove first elem in the string
                while (right - left) > len(p):
                    currLeft = s[left]
                    left += 1
                    currChars[currLeft] -= 1
                # If currChars == d, s[left:right] is an anagram of p
                if currChars == d:
                    result.append(left)
                right += 1
            else:
                currChars = {}
                left = right + 1
                right += 1
            
        return result