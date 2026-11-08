class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # establish how it will be broken into sub problems
        # base case
        # work out how the current answer depends on the previous answer
        # early exit if true
        n = len(s)
        # dp[x] where if dp[x] has a word, return true
        dp = [False] * (n+1) # broken into sub problems
        for i in range(n + 1):
            dp[i] = s[:i] in wordDict or any(s[j:i] in wordDict and dp[j] for j in range(1, n+1))
        return dp[n]

        
        