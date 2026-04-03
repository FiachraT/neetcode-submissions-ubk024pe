class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if number doesn't exist to the left of the number, it's the sart of a sequence
        # keep track of max sequence
        # O(N) Time, therefore no sorting
        num_set = set(nums)
        lenth = 0
        max_length = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length +=1
                max_length = max(length, max_length)
        return max_length


