class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = 0
        for n in nums:
            c = c ^ n
        return c
        