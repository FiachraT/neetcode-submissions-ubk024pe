class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # check that result exists
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)): # if result exists, what's the starting point
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res
        