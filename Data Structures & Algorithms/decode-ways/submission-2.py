class Solution:
    def numDecodings(self, s: str) -> int:
        #dp
        # each chr, make a decision to make chr or continue
        # no leading zeros
        # max numbr is 26
        
        # base case
        # 2 choices
        # 2nd choice has if statement
        dp = {len(s): 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            # first choice, single case
            res = dfs(i + 1)

            # second choice:
            if i + 1 < len(s) and (s[i] == "1" \
            or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
            
    



            


        
        