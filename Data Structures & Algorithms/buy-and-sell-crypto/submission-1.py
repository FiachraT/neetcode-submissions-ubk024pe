class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Can actually be greedy
        # key insight: each given day can be calculated as current price - min_index so far
        min_price = prices[0]
        max_output = 0
        for n in prices:
            min_price = min(min_price, n)
            profit = n - min_price
            max_output = max(max_output, profit)
        return max_output

        # Time Complexity O(N), space compexity O(1)

