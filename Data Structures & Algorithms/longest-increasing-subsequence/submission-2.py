class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # longest increasing subsequnece at that number
        # base case of first int
        # look at previous number before it that is smaller than it and increase by 1
        # keep max
        # return max
        n = len(nums)
        dp = [1] * (n +1)
        dp[0] = 1
        for i in range(1, n):
            num = nums[i]
            for j in range(i - 1, -1, -1):
                if nums[j] < num and dp[j] >= dp[i]:
                    dp[i] =dp[j] + 1
        return max(dp)