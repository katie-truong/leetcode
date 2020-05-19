import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Min heap to store the larger items:
        self.high = []
        # Max heap to store the smaller items:
        self.low = []

    def addNum(self, num: int) -> None:
        # Add number to self.low:
        heapq.heappush(self.low, -num)
        # Pop the largest item in self.low and add to self.high
        largest = heapq.heappop(self.low)
        heapq.heappush(self.high, -largest)
        # Balance if self.high has more items than self.low
        if len(self.high) > len(self.low):
            smallest = heapq.heappop(self.high)
            heapq.heappush(self.low, -smallest)

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        else:
            return -self.low[0]