class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # establish how it will be broken into sub problems
        # base case
        # work out how the current answer depends on the previous answer
        # early exit if true
        n = len(s)
        # dp[x] where if dp[x] has a word, return true
        words = set(wordDict)
        dp = [False] * (n+1) # broken into sub problems
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[n]

        
        