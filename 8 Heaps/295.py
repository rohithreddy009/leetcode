import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None: # 0(log n)
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.maxHeap , -heapq.heappushpop(self.minHeap, -num)) 
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, num))

    def findMedian(self) -> float: # 0(1)
        if len(self.minHeap) == len(self.maxHeap):
            return float(self.maxHeap[0] - self.minHeap[0]) / 2.0
        else:
            return float(self.maxHeap[0])
