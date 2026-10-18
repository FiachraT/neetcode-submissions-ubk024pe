import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      # create maxHeap
      #pop largest disance point greater than k
      maxHeap = []
      for x, y in points:
        # [-dist, point]
        heapq.heappush(maxHeap, ([-(x**2 + y**2), [x, y]]))
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
      return [p for d, p in maxHeap]
        




        