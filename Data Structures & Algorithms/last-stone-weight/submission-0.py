import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # find the top 2 largest ints in a list
        # remove both from list and add their difference as a val
        # continue until there is only 1 element left
        l = len(stones)
        weights= [0] * l
        for i in range(l):
            weights[i] = -stones[i]
        heapq.heapify(weights)
        # weights are negative
        while len(weights) > 1:
           x = heapq.heappop(weights)
           y = heapq.heappop(weights)
           heapq.heappush(weights, -abs(x - y))
        return -weights[0]
          
        
            