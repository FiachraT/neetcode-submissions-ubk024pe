class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #can't modify the array
        # O(1) memory (no lists, no maps)
        # Think of it like linked list cycle detection problem where you have to find the opening of the cycle
        #pointer = nums[pointer]
        # nums has to be at least 2 integers
        p1 = 0
        p2 = 0
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1==p2:
                break
        p2 = 0
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1

        
