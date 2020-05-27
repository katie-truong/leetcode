class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1 or dislikes == []:
            return True
        
        d = collections.defaultdict(set)

        for u, v in dislikes:
            d[u].add(v)
            d[v].add(u)
            
        groups = [0] * (N+1)
            
        q = collections.deque([])
        
        for i in range(1, N+1):
            if groups[i] == 0:
                q.append((i, 1))
            while q:
                item = q.popleft()
                num, g = item[0], item[1]
                for disliked in d[num]:
                    if groups[disliked] == g:
                        return False
                groups[num] = g
                new_g = 1 if g == 2 else 2
                for disliked in d[num]:
                    if groups[disliked] == 0:
                        q.append((disliked, new_g))
                    
        return True
            
            