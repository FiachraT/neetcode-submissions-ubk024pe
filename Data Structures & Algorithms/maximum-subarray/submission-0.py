class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window
        # greedy

        max_sub = nums[0]
        sum = 0
        for r in range(len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[r]
            max_sub =  max(sum, max_sub)
        return max_sub
            


