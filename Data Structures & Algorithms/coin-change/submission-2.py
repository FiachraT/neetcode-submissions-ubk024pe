class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # strucur of dynamic programming:
        # make a choice
        # undo choice, make a different choice
        #break large problem into many subproblems
        # top down and bottom up

        # sort coins
        # start from largest, if not move onto next, keep count
        # dfs

        #bottom up
        # dp[x] == minimum coins to get to x
        
       
        dp = [float("inf")]*(amount + 1)
        dp[0] = 0
        for cur_amount in range(1, amount + 1):
            for coin in coins:
                if cur_amount - coin >= 0:
                    dp[cur_amount] = min(dp[cur_amount], 1 + dp[cur_amount - coin] )
        return dp[amount] if dp[amount] != float("inf") else -1
        
        

        
        