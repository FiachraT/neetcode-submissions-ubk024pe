class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #price on any given day is the price[i] - current smallest stock
        cs = prices[0]
        max_profit = 0
        for c in prices:
            if c < cs:
                cs = c
            max_profit = max(c - cs, max_profit)
        return max_profit

        