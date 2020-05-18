class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        
        h = []
        
        for elem in counts:
            heapq.heappush(h, (counts[elem], elem))
            
        klargest = heapq.nlargest(k, h)
        
        result = []
        
        for item in klargest:
            result.append(item[1])
        
        return result