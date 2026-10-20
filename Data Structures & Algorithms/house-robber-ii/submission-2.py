class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 choices
        # rob the house, move to i + 2
        # don't rob the house, move to i + 1
        # if last house, compare with first house, take larger difference of 2
        #2 linear subproblems:
        # rob houses excluding the first
        # rob houses excluding the last
        def helper(nums) -> int:
            rob1, rob2 = 0, 0
            for num in nums:
                t = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = t
            return rob2
        
        if len(nums) <= 1:
            return nums[0]
        return max(helper(nums[: -1]), helper(nums[1:]))
            