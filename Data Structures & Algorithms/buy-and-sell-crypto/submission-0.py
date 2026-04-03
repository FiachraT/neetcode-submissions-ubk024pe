class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # being greedy coud hurt me therefore not greedy
        # key insight: each given day can be calculated as current price - min_index so far
        min_price = float("inf")
        max_output = 0
        for n in prices:
            min_price = min(min_price, n)
            day = n - min_price
            max_output = max(max_output, day)
        return max_output

