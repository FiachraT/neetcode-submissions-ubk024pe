class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        for i in range(1, n + 1):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return cost[n]
        
        