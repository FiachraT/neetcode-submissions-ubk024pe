import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # find the top 2 largest ints in a list
        # remove both from list and add their difference as a val
        # continue until there is only 1 element left
        l = len(stones)
        weights= [-s for s in stones]
        heapq.heapify(weights)
        print(weights)
        # weights are negative
        while len(weights) > 1:
           x = heapq.heappop(weights) # -2
           y = heapq.heappop(weights) # -1
           # x will always be larger or equal to y
           if x < y:
              heapq.heappush(weights, x - y)
        weights.append(0)
        return -weights[0]
          
        
            