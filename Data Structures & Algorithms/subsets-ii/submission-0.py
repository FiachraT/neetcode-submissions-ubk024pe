class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ##res
        # subset
        #enter loop
        # add subset to recurse if condition met
        ## make a choice (add)
        # recurse
        #undo that choice
        # recurse/ for loop
        # visited tracke?

        res = []
        nums.sort()
        subset = []

        def dfs(start):
            if start ==len(nums):
                res.append(subset.copy())
                return
        
            subset.append(nums[start])
            dfs(start + 1)
            subset.pop()
            while start + 1 < len(nums) and nums[start] == nums[start+1]:
                start+= 1
            dfs(start + 1)
            

        dfs(0)
        return res
        