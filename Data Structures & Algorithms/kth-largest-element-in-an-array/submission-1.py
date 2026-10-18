import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # negative 
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, n)
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
 
        return maxHeap[0]
        