class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force is to make a set and see max number after every number in the set. Start with minimum, remove after each loop:
        s = set(nums)
        max_count = 0
        current_count = 0
        while s or max_count < len(s):
            i = min(s)
            n = i
            while n in s:
                current_count += 1
                n +=1
            max_count = max(max_count,  current_count)
            current_count = 0
            s.remove(i)
        return max_count
        
