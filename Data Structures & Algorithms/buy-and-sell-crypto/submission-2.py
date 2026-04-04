class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # key insight: profi on any given day is current - current minimum
        # O(N)
        minN = prices[0]
        max_prof = 0
        for num in prices:
            minN = min(minN, num)
            profit = num - minN
            max_prof = max(max_prof, profit)
        return max_prof

        